<h1>Split Search Algorithm</h1>

<p>This repository demonstrates the <strong>Split Search Algorithm</strong>, a divide-and-conquer approach to find a specific element within an unsorted array. Unlike traditional binary search, Split Search can handle unsorted data by recursively dividing the array and narrowing down the search space. The project includes both a <strong>Python implementation</strong> of the algorithm and an <strong>HTML visualization</strong> to illustrate how the algorithm works.</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#how-it-works">How It Works</a></li>
  <li><a href="#files-in-the-repository">Files in the Repository</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2 id="overview">Overview</h2>
<p>Split Search is a custom search algorithm inspired by the binary search method but designed to work with <strong>unsorted arrays</strong>. It uses the divide-and-conquer technique to locate an element, effectively splitting the array into smaller segments and processing each segment independently. This approach increases efficiency for certain unsorted datasets compared to linear search.</p>

<h2 id="how-it-works">How It Works</h2>
<ol>
  <li><strong>Splitting</strong>: The algorithm divides the unsorted array into two halves.</li>
  <li><strong>Recursive Search</strong>: Each half is then searched recursively to locate the target element.</li>
  <li><strong>Divide and Conquer</strong>: This recursive splitting continues until the target element is found or the search space is exhausted.</li>
</ol>
<p>The algorithm’s divide-and-conquer approach makes it useful for specific unsorted search problems, especially those where restructuring the data is not feasible.</p>

<h2 id="files-in-the-repository">Files in the Repository</h2>
<ul>
  <li><code>split_search.py</code>: The Python script that contains the implementation of the Split Search Algorithm.</li>
  <li><code>index.html</code>: A visualization tool for the algorithm, which provides an interactive demonstration of how the search operates on an unsorted array.</li>
</ul>

<h2 id="installation">Installation</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/your-username/split-search-algorithm.git
cd split-search-algorithm
    </code></pre>
  </li>
  
  <li>Open <code>index.html</code> in a web browser to view the algorithm visualization.</li>
</ol>

<h2 id="usage">Usage</h2>
<h3>Running the Python Code</h3>
<p>To execute the Split Search in Python, run:</p>
<pre><code>python split_search.py
</code></pre>
<p>You can modify the array and target element within the <code>split_search.py</code> file.</p>

<h3>Viewing the HTML Visualization</h3>
<ol>
  <li>Open <code>index.html</code> in any modern web browser.</li>
  <li>Input an array and a target element in the provided fields.</li>
  <li>Click the "Search" button to visualize the split search process.</li>
</ol>



<h2 id="license">License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>
