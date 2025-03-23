A very basic, local library catalogue for use in my home library. Current ILS software is _way_ too extensive for simple home library needs.
Other software (e.g. goodreads) are all online, I prefer to have a local-only solution.

Features:
<ul>
<li>add books to 'database' (currently a .csv file) based on ISBN search</li>
<li>search owned books</li>
<li>view list of books</li>
<li>delete books from collection</li>
</ul>
Currently command line/terminal-only. 

Currently planned features/fixes:
<ul>
<li>book counts (in case of multiple copies)</li>
<li>book ratings</li>
<li>mark as read/not read</li>
<li>suggest random unread book</li>
<li>optional web frontend(flask?) but maintain CLI for classic look too. </li>
<li>book illustrations (if front-end implemented).</li>
<li>add books without isbn</li>
<li>book summaries (where available)</li>
<li>sanitize text output in order for WYSE font to properly generate (e.g. ë vs e)</li>
<li>further attempts to resemble Dynix/wyse classic terminal, including more smooth scrolling </li>
</ul>
