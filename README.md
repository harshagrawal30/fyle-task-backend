# fyle-task-backend

<h1>Steps to run  the backend</h1>
<ul>
<li>Fork and pull the repository to local machine</li>
<li>Open project directory in terminal and Make virtual environment using command "mkvirtualenv env-name" and then enter in env-name using "workon env-name"</li>
<li>After creating virtual environment install the dependencies present in software.txt file using command "pip install -r software.txt"</li>
<li>Make migrations using "python manage.py makemigrations" and then "python manage.py migrate" command. (Optional to setup database)</li>
<li>Finally, Start app using "python manage.py runserver"</li>
<p>Now go to url "http://localhost:8000/user/api/user/{{username}}" to see the fetched result.
