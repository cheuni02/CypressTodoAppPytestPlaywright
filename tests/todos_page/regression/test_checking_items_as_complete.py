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
    def setup(self, page: Page):
        listPotentialTasks = [
            "feed the goldfish",
            "call your best friend",
            "have a haircut",
            "cook your girlfriend something nice",
            "fill up the petrol",
            "take the trash out",
            "jog up to 5km"
        ]
        todosPage = TodosPage(page)
        todosPage.goto()
        for task in listPotentialTasks:
            todosPage.enterItem(task)
        yield SetupContext(
            page = todosPage,
            listTasks = listPotentialTasks
        )
        page.context.clear_cookies()

    def test_marking_one_task_as_complete(self, setup, page: Page):
        tasks = setup.listTasks
        selectedTask = tasks[random.randrange(len(tasks))]
        print(f"selectedTask: {selectedTask}")

        expect(setup.page.getItemLabelled(selectedTask)).not_to_have_class("completed")
        setup.page.getItemToggleButton(selectedTask).click()
        expect(setup.page.getItemLabelled(selectedTask)).to_have_class("completed")
