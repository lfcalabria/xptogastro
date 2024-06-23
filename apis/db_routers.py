DATABASE_APPS_MAPPING = {
    'apis': 'mysql_db',
}


class DatabaseRouter:
    def db_for_read(self, model, **hints):
        return DATABASE_APPS_MAPPING.get(model._meta.app_label, 'default')

    def db_for_write(self, model, **hints):
        return DATABASE_APPS_MAPPING.get(model._meta.app_label, 'default')

    def allow_relation(self, obj1, obj2, **hints):
        db_obj1 = DATABASE_APPS_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_APPS_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            return db_obj1 == db_obj2
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Se a aplicação é 'apis', ela deve usar o banco de dados MySQL
        if app_label in DATABASE_APPS_MAPPING:
            return DATABASE_APPS_MAPPING[app_label] == db
        # Para todas as outras aplicações (incluindo tabelas internas do Django), usar o banco de dados padrão (SQLite)
        return db == 'default'
