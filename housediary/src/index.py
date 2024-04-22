from ui.diary_first_ui import HouseDiary
from repositories.user_repository import UserRepository
from repositories.tasks_repository import UnscheduledTasksRepository, ScheduledTasksRepository
from services.house_diary_service import HouseDiaryService
from database_connection import get_database_connection


def main():

    database_connection = get_database_connection()

    user_repository = UserRepository(database_connection)

    unscheduled_tasks_repository = UnscheduledTasksRepository(
        database_connection)

    scheduled_task_repository = ScheduledTasksRepository(
        database_connection)

    house_diary_service = HouseDiaryService(
        user_repository, unscheduled_tasks_repository, scheduled_task_repository)

    house_diary_app = HouseDiary(house_diary_service)
    house_diary_app.start()


if __name__ == "__main__":
    main()
