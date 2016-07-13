import web


class PageHandler(web.HTTPHandler):
    directory = '.'
    page = 'index.html'

    def format(self, page):
        return page

    def do_get(self):
        self.response.headers.set('Content-Type', 'text/html')

        with open(self.directory + '/' + self.page, 'r') as file:
            page = file.read()

        return 200, self.format(page)


class ErrorPageHandler(web.HTTPHander):
    directory = '.'
    page = 'error.html'

    def format(self, page):
        if self.error.status_message:
            status_message = self.error.status_message
        else:
            status_message = web.status_messages[self.error.code]

        if self.error.message:
            message = self.error.message
        else:
            message = str(self.error.code) + ' - ' + status_message + '\n'

        return page.format(code=self.error.code, status_message=status_message, message=message)

    def respond(self):
        self.response.headers.set('Content-Type', 'text/html')

        with open(self.directory + '/' + self.page, 'r') as file:
            page = file.read()

        return 200, self.format(page)
