from selenium import webdriver


class RoomBooker:
    def __init__(self, parameters, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.PhantomJS()
        self.parameters = parameters
        self.page_name = "https://raumbuchung.ub.uni-marburg.de"

    def login_and_book(self):
        self.login()
        self.create_booking()

    def login(self):
        driver = self.driver
        driver.get(self.page_name)
        driver.find_element_by_id('global-login-button').click()
        driver.find_element_by_id('username').send_keys(self.username)
        driver.find_element_by_id('password').send_keys(self.password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def create_booking(self):
        params = self.parameters
        value = [params[x] for x in params]
        value = ','.join(value)
        jscode = self._build_request('book_room', value)
        response = self.driver.execute_script(jscode)
        print(response)

    def delete_booking(self):
        params = self.parameters
        value = [params['date'], params['start'], params['room_number']]
        value = ','.join(value)
        jscode = self._build_request('delete', value)
        response = self.driver.execute_script(jscode)
        print(response)

    def _build_request(self, action, value):
        b_url = "/ajax_php/set_data.php?action={}&value=".format(action)
        jscode = """var request=new XMLHttpRequest();
                    request.open('GET', '{}{}',false);
                    request.send();
                    return request.responseText""".format(b_url, value)
        return jscode
