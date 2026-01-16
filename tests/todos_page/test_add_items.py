import math
import random
from dataclasses import dataclass

import pytest
from playwright.sync_api import Page, expect

from pages.todosPage import TodosPage

@dataclass
class TodosContext:
    page: TodosPage
    item: str

class TestAddItems:
    @pytest.fixture(scope="function")
    def setup(self, page: Page):
        itemTobeAdded = "hoover"
        todosPage = TodosPage(page)
        todosPage.goto()
        expect(todosPage.todoListItem(itemTobeAdded)).not_to_be_visible()
        todosPage.enterItem(itemTobeAdded)
        yield TodosContext(
            page = todosPage,
            item = itemTobeAdded,
        )
        page.context.clear_cookies()

    def test_adding_single_appends_it_to_list(self, setup):
        expect(setup.page.todoListItem(setup.item)).to_be_visible()

    def test_todo_count_incremented_once_item_added(self, setup):
        expect(setup.page.getTodoCount()).to_have_text("3 items left")

    def test_3_items_shown_after_1_added(self, setup):
        assert len(setup.page.getTodoListItems()) == 3

    def test_add_n_more_items(self, setup) -> None:
        listPotentialTasks = [
            "feed the goldfish",
            "walk the dog",
            "have a haircut",
            "cook your girlfriend something nice",
            "fill up the petrol",
            "take the trash out",
            "jog up to 5km"
        ]

        randomNumberToAdd = random.randrange(1, len(listPotentialTasks))
        expectedNumItems = 3 + randomNumberToAdd
        expectedTodoCountMsg = f"{expectedNumItems} items left"
        toBeAdded = []
        while randomNumberToAdd > 0:
            selectedTask = random.choice(listPotentialTasks)
            while selectedTask in toBeAdded:
                selectedTask = random.choice(listPotentialTasks)
            toBeAdded.append(selectedTask)
            randomNumberToAdd -= 1

        for item in toBeAdded:
            setup.page.enterItem(item)

        expect(setup.page.getTodoCount()).to_have_text(expectedTodoCountMsg)
        expectedNumberTodoItems = len(setup.page.getTodoListItems())
        assert expectedNumberTodoItems == expectedNumItems

