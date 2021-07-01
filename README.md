<h1 class="gap">0x00. AirBnB clone - The console</h1>

<h2>Supported classes:</h2>
<ul>
    <li>BaseModel</li>
    <li>User</li>
    <li>State</li>
    <li>Place</li>
    <li>Review</li>
    <li>City</li>
    <li>Amenity</li>
</ul>

<h2>Comands:</h2>
<ul>
    <li>create - create an object</li>
    <li>show - show an object (based on id)</li>
    <li>destroy - destroy an object</li>
    <li>all - show all objects, of one type or all types</li>
    <li>quit/EOF - quit the console</li>
    <li>help - see descriptions of commands</li>
</ul>

<p>To start, navigate to the project folder and enter <b>./console.py</b> in the shell.</p>
<h3>create</h3>
<code>create "class name" </class></code><p>EX: </p> <code>create BaseModel</code>

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