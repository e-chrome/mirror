import uuid
from datetime import datetime

from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    timezone = None

    def add_fields(self, log_record, record, message_dict):
        extra_dict = self.create_extra_dict(record)

        def form_fields():
            if record.args:
                msg = str(record.msg) % record.args
            else:
                msg = str(record.msg)

            return {'id': uuid.uuid4(), 'ts': self.format_datetime(record), 'level': record.levelname, 'msg': msg}

        fields_dict = form_fields()

        if extra_dict:
            fields_dict['context'] = extra_dict

        log_record.update(fields_dict)

    def format_datetime(self, record: int) -> str:
        if not self.timezone:
            self.set_timezone()
        log_created_as_datetime = datetime.fromtimestamp(record.created, tz=self.timezone)
        return log_created_as_datetime.isoformat()

    def set_timezone(self):
        now = datetime.now()
        local_now = now.astimezone()
        self.timezone = local_now.tzinfo

    def create_extra_dict(self, record) -> dict:
        extra_dict = {}
        for key, value in record.__dict__.items():
            # this allows to have numeric keys
            if key not in self._skip_fields and not (hasattr(key, 'startswith') and key.startswith('_')):
                extra_dict[self.rename_fields.get(key, key)] = value
        return extra_dict
