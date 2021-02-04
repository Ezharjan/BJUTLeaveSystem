from marshmallow import Schema, fields, validates


fields.Field.default_error_messages = {
    'invalid': '不是合法数字',
    'required': '缺少必填数据',
}


class LeaveBeijingSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    student_id = fields.String(required=True)
    colleage = fields.String(required=True)
    id_card = fields.String(required=True)
    leave_time = fields.String(required=True)
    back_time = fields.String(required=True)
    counselor = fields.String(required=True)
    transportation = fields.String(required=True)
    telephone = fields.String(required=True)
    healthy = fields.String(required=True)
    reason = fields.String(required=True)
    destination = fields.String(required=True)
    create_time = fields.String()
    update_time = fields.String()
    is_del = fields.Bool()


leave_beijing_list_schema = LeaveBeijingSchema(many=True)
leave_beijing_add_schema = LeaveBeijingSchema()
leave_beijing_detail_schema = LeaveBeijingSchema()

