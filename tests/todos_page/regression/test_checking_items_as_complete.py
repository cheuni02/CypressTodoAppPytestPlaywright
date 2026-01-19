import random
from dataclasses import dataclass

import pytest
from playwright.sync_api import Page, expect

from pages.todosPage import TodosPage

@dataclass
class SetupContext:
    page: TodosPage
    listTasks: list

class TestCheckingItemAsComplete:
    @pytest.fixture(scope='function')
    def setup(self, todosListFixture: list[str], page: Page):
        todosPage = TodosPage(page)
        todosPage.goto()
        for task in todosListFixture:
            todosPage.enterItem(task)
        yield SetupContext(
            page = todosPage,
            listTasks = todosListFixture
        )
        page.context.clear_cookies()

    def test_marking_one_task_as_complete(self, setup: SetupContext):
        tasks = setup.listTasks
        selectedTask = tasks[random.randrange(len(tasks))]
        expect(setup.page.todoListItem(selectedTask)).not_to_have_class("completed")
        setup.page.getItemToggleButton(selectedTask).click()
        expect(setup.page.todoListItem(selectedTask)).to_have_class("completed")

    def test_marking_two_or_more_task_as_complete(self, setup: SetupContext):
        totalTasksAdded = 2 + len(setup.listTasks)
        numberOfTasksToComplete = random.randrange(2,len(setup.listTasks))
        listTasksToComplete = []
        for _ in range(numberOfTasksToComplete):
            randomTask = setup.listTasks[random.randrange(len(setup.listTasks))]
            while randomTask in listTasksToComplete:
                randomTask = setup.listTasks[random.randrange(len(setup.listTasks))]
            listTasksToComplete.append(randomTask)
        for task in listTasksToComplete:
            setup.page.getItemToggleButton(task).click()
        assert len(setup.page.getTodoListItems()) == totalTasksAdded
        expect(setup.page.getTodoCount()).to_have_text(f"{totalTasksAdded - numberOfTasksToComplete} items left")