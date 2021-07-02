<img src="hbnb.png" alt="">

<h1 class="gap">0x00. AirBnB clone - The console</h1>

<h2>About AirBnB clone - The console:</h2>
<p>This is a command interpreter to manipulate data for the web page HBnB without a visual interface. The console will create data model, manage (create, update, destroy, etc) objects via a console / command interpreter and store and persist objects to a file (JSON file)</p>
<p>The console will be a tool to validate the storage engine</p>

<h2>About The Command Interpreter:</h2>
<p>With the console you have can manage the objects of this project</p>


<h3>Supported classes:</h3>
<ul>
    <li>BaseModel</li>
    <li>User</li>
    <li>State</li>
    <li>Place</li>
    <li>Review</li>
    <li>City</li>
    <li>Amenity</li>
</ul>

<h3>Comands:</h3>
<ul>
    <li>create - create an object</li>
    <li>show - show an object (based on id)</li>
    <li>destroy - destroy an object</li>
    <li>all - show all objects, of one type or all types</li>
    <li>quit/EOF - quit the console</li>
    <li>help - see descriptions of commands</li>
</ul>

<p>To start, navigate to the project folder and enter <b>./console.py</b> in the shell.</p>
 <h4>create</h4>
    <pre><code>create "class name"</code></pre>
    <p>EX: </p><code>$ create BaseModel</code>
 <h4>show</h4>
    <pre><code>show "class name" "id"</code></pre>
    <p>EX: </p><code>$ show BaseModel 1234-1234-1234</code>
 <h4>destroy</h4>
    <pre><code>destroy "class name"</code></pre>
    <p>EX: </p><code>$ destroy BaseModel 1234-1234-1234</code>
 <h4>all</h4>
    <pre><code>all "class name" , or: all</code></pre>
    <p>EX: </p> <code>$ all BaseModel</code>
 <h4>update</h4>
    <pre><code>update "class name" "id" "attribute" "value of attribute"</code></pre>
    <p>EX: </p> <code>$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"</code>
 <h4>help</h4>
    <pre><code>help</code></pre>
    <p>EX: </p> <code>help</code>

<h2>More Info</h2>

<h3>Execution</h3>

<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
</code></pre>

<p>But also in non-interactive mode: (like the Shell project in C)</p>

<pre><code>$ echo "help" | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb)
$
</code></pre>

<p>All tests should also pass in non-interactive mode: <code>$ echo "python3 -m unittest discover tests" | bash</code></p>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210624%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210624T143900Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=52ec2bc9931ff114669768867a3215d3b423e63ef7c16fce9f1b42b9d21a91dc" alt=""></p>

</div>
<h2>Flowchart</h2>

<img src="image.png" alt="">
<br>
<h2>Authors</h2>
<p>David Cera jdcera@gmail.com</p>
<p>Paula Louvani Hernandez paula.louvani@gmail.com</p>

