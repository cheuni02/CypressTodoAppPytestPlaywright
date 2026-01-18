import pytest
from playwright.sync_api import Page, expect
from pages.todosPage import TodosPage


class TestLookAndFeel():

    @pytest.fixture(scope="function", name="todosPage")
    def setup(self, page: Page):
        todosPage = TodosPage(page)
        todosPage.goto()
        yield todosPage
        page.context.clear_cookies()

    def test_that_2_jobs_are_already_displayed(self, todosPage) -> None:
        expect(todosPage.todoListItem("Pay electric bill")).to_be_visible()
        expect(todosPage.todoListItem("Walk the dog")).to_be_visible()

    def test_list_footer_shows_2_jobs_remaining(self, todosPage) -> None:
        expect(todosPage.getTodoCount()).to_have_text("2 items left")

    def test_list_footer_shows_3_filters_and_all_selected(self, todosPage) -> None:
        filterButtons = {"All", "Active", "Completed"}
        for filterButton in filterButtons:
            expect(todosPage.getFilters()).to_contain_text(filterButton)
            if filterButton == "All":
                expect(todosPage.getFilterButton(filterButton)).to_have_class("selected")
                continue
            expect(todosPage.getFilterButton(filterButton)).not_to_have_class("selected")

    def test_placeholder_shows_on_input(self, todosPage) -> None:
        expect(todosPage.getInputBox()).to_have_attribute("placeholder", "What needs to be done?")

    def test_input_box_is_clear_when_page_first_loads(self, todosPage) -> None:
        expect(todosPage.getInputBox()).to_be_empty()
