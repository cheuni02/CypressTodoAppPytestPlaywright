import pytest
from playwright.sync_api import Page, expect
from pages.todosPage import TodosPage

class TestRemoveItems:
    @pytest.fixture(scope="function", name="todosPage")
    def setup(self, page: Page):
        todosPage = TodosPage(page)
        todosPage.goto()
        yield todosPage
        page.context.clear_cookies()

    def test_remove_item_via_X_button(self, todosPage: TodosPage):
        itemLabel = "Pay electric bill"
        itemXbutton = todosPage.getTodoDestroyButton(itemLabel)
        assert len(todosPage.getTodoListItems()) == 2
        todosPage.todoListItem(itemLabel).hover()
        expect(itemXbutton).to_be_visible()
        itemXbutton.click()
        assert len(todosPage.getTodoListItems()) == 1
        expect(todosPage.todoListItem("Walk the dog")).to_be_visible()