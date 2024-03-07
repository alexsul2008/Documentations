class Responses:
    """Sets responsers color and message."""

    @staticmethod
    def raise_error_bd (responser, msg):
        responser.setStyleSheet('*{color: red; font: 10pt "Verdana"; padding: 0 10px;}')
        responser.setText(msg)

    @staticmethod
    def raise_error(responser, msg, field):
        responser.setStyleSheet('*{color: red;}')
        responser.setText(msg)
        if field:
            field.setStyleSheet('*{border: 2px solid red;}')


    @staticmethod
    def raise_alert(responser, msg):
        responser.setStyleSheet('*{color: orange;}')
        responser.setText(msg)

    @staticmethod
    def success_message(responser, msg, time):
        responser.setStyleSheet('*{color: green;}')
        responser.setText(msg, time)

    @staticmethod
    def error_message_status_bar (responser, msg, time):
        responser.setStyleSheet('*{color: red; font: 10pt "Verdana"; padding: 0 10px;}')
        responser.showMessage(msg, time)

    @staticmethod
    def success_message_status_bar(responser, msg, time):
        responser.setStyleSheet('*{color: green; font: 10pt "Verdana"; padding: 0 10px;}')
        responser.showMessage(msg, time)

    @staticmethod
    def clear(inputs, responser=None):
        """
        Clear inputs and responsers
        """
        for input_ in inputs:
            input_.setText('')
        if responser is None:
            return
        responser.setText('')

    @staticmethod
    def clear_msg(parent, responser, bool):
        """
        Clear responsers
        """
        responser.setText('')
        parent.setHidden(bool)

    @staticmethod
    def clearInputs(parent, inputs_, exclusion=[]):
        # print('Кол-во исключаемых элементов: ', len(exclusion))
        for widget in parent.findChildren(inputs_):
            # print(widget.text())
            widget.clear()

    @staticmethod
    def message_from_db(status, from_show, msg):
        # print(status, from_show)
        if status == 'save':
            from_show.setStyleSheet('*{color: green;}')
            from_show.showMessage(msg, 10000)
        elif status == 'update':
            from_show.setStyleSheet('*{color: orange;}')
            from_show.showMessage(msg, 10000)
        elif status == 'deletes':
            from_show.setStyleSheet('*{color: green;}')
            from_show.showMessage(msg, 10000)
        elif status == 'error':
            from_show.setStyleSheet('*{color: red;}')
            from_show.showMessage('Что-то пошло не так!', 10000)



