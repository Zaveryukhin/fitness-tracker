from dataclasses import dataclass, asdict


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""

    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    message = (
               'Тип тренировки: {training_type};'
               ' Длительность: {duration:.3f} ч.;'
               ' Дистанция: {distance:.3f} км;'
               ' Ср. скорость: {speed:.3f} км/ч;'
               ' Потрачено ккал: {calories:.3f}.'
               )

    def get_message(self):
        """ Сформировать сообщение"""
        return self.message.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    min_in_hour: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        message = InfoMessage(self.__class__.__name__,
                              self.duration,
                              self.get_distance(),
                              self.get_mean_speed(),
                              self.get_spent_calories()
                              )
        return message


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def get_spent_calories(self) -> float:
        spent_calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER *
                           self.get_mean_speed()
                           + self.CALORIES_MEAN_SPEED_SHIFT)
                          * self.weight / self.M_IN_KM * self.duration
                          )
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 0.035
    CALORIES_MEAN_SPEED_SHIFT = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: int):
        self.height = height
        super().__init__(action, duration, weight)

    def get_spent_calories(self):
        cm_in_m = 100
        height_in_meters = self.height / cm_in_m
        spent_calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER *
                           self.weight +
                           (self.get_mean_speed() ** 2 /
                            height_in_meters) * 0.029 *
                           self.weight) * self.duration
                          )
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: int,
                 count_pool: int
                 ):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        mean_speed = (self.length_pool *
                      self.count_pool /
                      self.M_IN_KM /
                      self.duration
                      )
        return mean_speed

    def get_spent_calories(self):
        spent_calories = ((self.get_mean_speed() + 1.1)
                          * 2 * self.weight * self.duration)
        return spent_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_types = {'SWM': Swimming,
                     'RUN': Running,
                     'WLK': SportsWalking}
    training_data = workout_types[workout_type](*data)
    return training_data


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
