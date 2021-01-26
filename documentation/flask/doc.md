Route we flasku to funkcje z dekoratorem @app.route i adresem zapytania: 
```
@app.route('/paginate_data', methods=['POST'])
def backend_pagination():
    start = int(request.form['start'])
    length = int(request.form['length'])
    original_df = pd.read_csv('./tmp/output/download' + str(current_user.id) + '.csv', header=None)
    df = original_df.drop([0])
    df = df.iloc[start:start + length, :]
    for field in UrlFieldsEnum:
        df[field] = df[field].apply(add_links)
    return jsonify(data=json.loads(df.to_json(orient="records")), recordsTotal=len(original_df.index) - 1, recordsFiltered=len(original_df.index) - 1)
```
Tutaj przykładowe zapytanie pobierające informacje z forma requestowego. Na wyjściu json. 


STRUKTURA: 
w głównym folderze skrypty do uruchamiania api itd. 
W folderze app wszystkie routes. Moim zdaniem routes powinny być podzielone tematycznie na foldery, unikniemy bałaganu jaki ja miałem w swoim projekcie.
 Z 2 strony jeśli mamy też mieć tylko kilka zapytań to nie ma sensu robić bardzo skomplikowanej struktury. 
 Do organizacji struktury całego projektu można posłużyć się tym: 
 https://flask.palletsprojects.com/en/1.1.x/tutorial/views/




Procfile na heroku: 
```
web: python manage.py runserver --host 0.0.0.0 --port ${PORT}

init: python manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade
```
Skrypt odpalany przez heroku na starcie:
```
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config

from app import app, db


app.config.from_object(Config)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

```




Paczka do wykonywania zapytań do innych restów:
https://requests.readthedocs.io/en/master/

Przydatny tutorial z którego się uczyłem: 
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
