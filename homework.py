M_IN_KM: int = 1000
LEN_STEP: float = 0.65


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: int,
                 distance: int,
                 speed: int,
                 calories: int):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.; Дистанция: '
                f'{self.distance} км; Ср. скорость: {self.speed} км/ч; Потрачено ккал: {self.calories}.')


class Training:
    """Базовый класс тренировки."""

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

        distance = self.action * LEN_STEP / M_IN_KM
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
        pass


class Running(Training):
    """Тренировка: бег."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float):
        super().__init__(action)
        super().__init__(duration)
        super().__init__(weight)

    def get_spent_calories(self):
        spent_calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_mean_speed()
                           + self.CALORIES_MEAN_SPEED_SHIFT)
                          * self.weight / M_IN_KM * self.duration)
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    LEN_STEP: float = 1.38
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
