# HTML Templates

main_page_template = """
<!DOCTYPE html>
<html>
<head>
<link href="/assets/css/blog.css" rel="stylesheet" type="text/css">
<title>Bogdikon - blog</title>
</head>
<body>
<header>
<ul>
<li>
<a href="index.html">home</a>
</li>
<li>
<a href="blog">blog</a>
</li>
</ul>
</header>
<main>
<h1>Bogdikon's blog!</h1>
Welcome to Bogdikon's mini blog. I will post something here when I'm in mood.
<h1/>
<h3>Page {page}</h3>
{posts}
</main>
<footer>
<span>
<a href="about.html">Bogdikon</a>&#169; 2025
<div class="right">
{pages_links}
</div>
</span>
</footer>
</body>
</html>
"""

css = """/* originally written by Devine Lu Linvega */

* { margin:0;padding:0;text-decoration:none;box-sizing:border-box;color:#000 }
html { background-position:center;background-size:cover;background-color:#d8d8d8;min-height:100vh }
body { background-color:#fff;outline:2px solid #000;font-family:sans-serif;font-size:16px;max-width:700px;margin:50px auto;overflow-x:hidden }
body > *, body main > *, main figure > div > *, main p, main q, main cite, main pre { margin-bottom:20px }
body .right { float:right;margin:0 0 0 10px }
body a.self, body a.parent { font-style:italic }
main a:hover, main a:hover > *, nav a:hover, nav main a:hover > * { background-color:#000;color:#fff;text-decoration:none }
table td, table th { vertical-align:top;padding:2.5px 5px;text-align:left }
table td > pre, table th > pre { background:none;padding:0;margin:0 }
table tr img { margin-bottom:0 }
hr { clear:both;border:0 }
em { font-style:italic }
header { overflow-wrap:normal;padding:15px 30px;border-bottom:2px solid #000;clear:both;line-height:30px }
header ul { list-style-type:none }
header li { display:inline-block;padding:0;margin-right:30px }
header a:hover { text-decoration:underline }
header img { display:block }
nav { display:none;padding:25px 45px 0 0;margin:0 }
nav ul { padding:0;margin:0 30px 60px 0;display:inline-block;vertical-align:top }
nav ul li { list-style-type:none;white-space:pre }
nav ul li a { padding:0 4px }
main { overflow-wrap:break-word;margin:30px;clear:both }
main a { text-decoration:underline }
main a[target="_blank"] { text-decoration-style:dotted }
main article { border-left:1px dotted #000;padding-left:25px;clear:both }
main cite { display:block;clear:both }
main cite:before { content:"— " }
main iframe { width:100% }
main ul, main ol { margin:0 0 20px 30px }
main ul ul { margin-bottom:0 }
main ul li, main ol li { line-height:25px;padding:0 5px }
main figure img { display:block;margin:0 !important }
main figure figcaption { padding:15px 0 }
main p, main ul li, main ol li { line-height:160% }
main sup { line-height:12px }
main ::selection { background-color:#6b83a5;color:#fff;text-decoration:none }
main q { font-family:serif;font-size:18px;font-style:italic;display:block;max-width:450px }
main > img, main > svg, main figure > img, main figure > svg { max-width:100%;display:block;margin:0 0 25px 0 }
main pre { overflow:auto;background:#efefef;padding:10px;font-size:80% }
main pre code, main pre i { color:#888 }
main code { background-color:#eee;white-space:pre;font-size:15px }
main hr { clear:both }
main kbd { font-size:12px;display:inline-block;padding:0 5px;font-weight:bold;border-radius:4px;line-height:20px;border:2px solid #888 }
footer { padding:15px 0px 30px 0px;margin:0 30px;font-size:13px;line-height:30px;clear:both;border-top:1px dotted #000 }
footer a { display:inline-block;margin-right:3px }
footer a:hover { text-decoration:underline }
footer img { height:30px;vertical-align:middle;margin:0 3px }
footer div.right img { margin-left:10px }

@media (max-width:720px) {
	body { margin:50px 10px }
}
@media (max-width:700px) {
	header { padding:15px 20px }
	main { margin:30px 20px }
	footer { margin:0px 20px }
}
@media (prefers-color-scheme:dark) {
	* { color:#fff }
	html { background-color:#181818 }
	body { background:#000;outline-color:#fff }
	main a:hover, main a:hover > *, nav a:hover, nav a:hover > * { background-color:#fff;color:#000;text-decoration:none }
	main ::selection { background-color:#7c98bf;color:#000;text-decoration:none }
	main article { border-left:1px dotted #fff }
	main img.invert, footer img, header img { background:#fff;filter:invert(1) hue-rotate(180deg) }
	main pre { background:#111 }
	main code { background-color:#111 }
	main table { border-style:solid }
	main th, main td { border-style:dotted }
	header, footer { border-color:#fff }
}"""

post_template = """
<h2>{title}</h2>
<article>
{body}
</article>
<h6>- {timestamp}<h6>
"""

large_post_template = """
<h2>{title}</h2>
<article>
{body}
<br>
<a href="{full_post_link}">See more...</a>
</article>
<h6>- {timestamp}<h6>
"""

full_post_template = """
<!DOCTYPE html>
<html>
<head>
<link href="/assets/css/blog.css" rel="stylesheet" type="text/css">
<title>Bogdikon - blog</title>
</head>
<body>
<header>
<ul>
<li>
<a href="index.html">home</a>
</li>
<li>
<a href="blog">blog</a>
</li>
</ul>
</header>
<main>
<h2>{title}</h2>
{body}
<br>
<br>
<h6>- {timestamp}<h6>
</main>
<footer>
<span>
<a href="about.html">Bogdikon</a>&#169; 2025
</span>
</footer>
</body>
</html>
"""

error_template = """
<!DOCTYPE html>
<html>
<head>
<link href="/assets/css/blog.css" rel="stylesheet" type="text/css">
<title>Bogdikon - blog</title>
</head>
<body>
<header>
<ul>
<li>
<a href="index.html">home</a>
</li>
<li>
<a href="blog">blog</a>
</li>
</ul>
</header>
<main>
<h3>{error_text}</h3>
</main>
<footer>
<span>
<a href="about.html">Bogdikon</a>&#169; 2025
</span>
</footer>
</body>
</html>
"""