from operator import contains

from playwright.sync_api import Page, Locator

class TodosPage:
    def __init__(self, page: Page):
        self.page = page
        self.todoApp = self.page.locator(".todoapp")
        self.pageHeader = self.todoApp.locator("header h1")
        self.inputBox = self.todoApp.locator("input[data-test='new-todo']")
        self.toggleAll = self.page.locator(".main label[for='toggle-all']")
        self.todoList = self.page.locator("ul.todo-list")
        self.todoListItems = self.todoList.locator("li")
        self.checkboxesComplete = self.todoListItems.locator("input.toggle")
        self.footer = self.todoApp.locator("footer")
        self.todoCount = self.footer.locator(".todo-count")
        self.filters = self.footer.locator(".filters")

    def goto(self):
        self.page.goto("/todo")

    def getInputBox(self):
        return self.inputBox

    def clickToggleAll(self):
        self.toggleAll.click()

    def enterItem(self, item: str):
        self.inputBox.fill(item)
        self.inputBox.press('Enter')

    def getTodoListItems(self):
        return self.todoListItems.all()

    def todoListItem(self, label: str) -> Locator:
        return self.todoList.locator(
            "li",
            has=self.page.locator("label", has_text=label)
        )

    def getHeader(self) -> Locator:
        return self.pageHeader

    def getTodoApp(self):
        return self.todoApp

    def getFilters(self):
        return self.filters

    def getFilterButton(self, label: str) -> Locator:
        return self.filters.locator(
            "a",
            has_text=label
        )

    def getTodoCount(self) -> Locator:
        return self.todoCount

    def getTodoCheckbox(self, task):
        todo_li = self.todoList.locator(
            "li",
            has=self.page.locator("label", has_text=task)
        )
        return todo_li.locator("input.toggle")

    def getTodoDestroyButton(self, task):
        todo_li = self.todoList.locator(
            "li",
            has=self.page.locator("label", has_text=task)
        )
        return todo_li.locator("button")

    def getTestButton(self, task):
        print(task)
        return self.todoList.locator(
            "li:nth-child(2) button.destroy",
        )