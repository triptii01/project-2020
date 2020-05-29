page = '<a href="www.hi.com">hi</a>'

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
       return None, 0
    else:
       start_quote = page.find('"', start_link)
       end_quote = page.find('"', start_quote + 1)
       url = page[start_quote + 1 : end_quote]
       
       return url, end_quote

#url, endpos = get_next_target(page)
#if url:             
#  print("here!")
#else:
#  print("not here!")


def print_all_links(page):
       while True:
            url, endpos = get_next_target(page)
            if url:
                 print(url)
                 page = page[endpos:]
            else:
                 break

print_all_links(""" <!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>Web development - Wikipedia</title>
<script>document.documentElement.className="client-js";RLCONF={"wgBreakFrames":!1,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"Xr@BKwpAEJkAAhzHvAwAAABD","wgCSPNonce":!1,"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":!1,"wgNamespaceNumber":0,"wgPageName":"Web_development","wgTitle":"Web development","wgCurRevisionId":940071839,"wgRevisionId":940071839,"wgArticleId":611714,"wgIsArticle":!0,"wgIsRedirect":!1,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["Wikipedia indefinitely semi-protected pages","Articles needing additional references from December 2012","All articles needing additional references","Wikipedia articles with style issues from September 2018","All articles with style issues","Wikipedia articles with LCCN identifiers","Web development"],
"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgRelevantPageName":"Web_development","wgRelevantArticleId":611714,"wgIsProbablyEditable":!1,"wgRelevantPageIsProbablyEditable":!1,"wgRestrictionEdit":["autoconfirmed"],"wgRestrictionMove":["autoconfirmed"],"wgMediaViewerOnClick":!0,"wgMediaViewerEnabledByDefault":!0,"wgPopupsReferencePreviews":!1,"wgPopupsConflictsWithNavPopupGadget":!1,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en"},"wgMFDisplayWikibaseDescriptions":{"search":!0,"nearby":!0,"watchlist":!0,"tagline":!1},"wgWMESchemaEditAttemptStepOversample":!1,"wgULSCurrentAutonym":"English","wgNoticeProject":"wikipedia","wgWikibaseItemId":"Q386275","wgCentralAuthMobileDomain":!1,"wgEditSubmitButtonLabelPublish":!0};RLSTATE={"ext.globalCssJs.user.styles":"ready","site.styles":"ready","noscript":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","user":"ready","user.options":"loading",
"ext.cite.styles":"ready","mediawiki.toc.styles":"ready","skins.vector.styles.legacy":"ready","wikibase.client.init":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","ext.wikimediaBadges":"ready"};RLPAGEMODULES=["ext.cite.ux-enhancements","site","mediawiki.page.startup","skins.vector.js","mediawiki.page.ready","mediawiki.toc","ext.gadget.ReferenceTooltips","ext.gadget.charinsert","ext.gadget.refToolbar","ext.gadget.extra-toolbar-buttons","ext.gadget.switcher","ext.centralauth.centralautologin","mmv.head","mmv.bootstrap.autostart","ext.popups","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.compactlinks","ext.uls.interface","ext.cx.eventlogging.campaigns","ext.quicksurveys.init","ext.centralNotice.geoIP","ext.centralNotice.startUp"];</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.loader.implement("user.options@1hzgi",function($,jQuery,require,module){/*@nomin*/mw.user.tokens.set({"patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
});});</script>
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=ext.cite.styles%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cmediawiki.toc.styles%7Cskins.vector.styles.legacy%7Cwikibase.client.init&amp;only=styles&amp;skin=vector"/>
<script async="" src="/w/load.php?lang=en&amp;modules=startup&amp;only=scripts&amp;raw=1&amp;skin=vector"></script>
<meta name="ResourceLoaderDynamicStyles" content=""/>
<link rel="stylesheet" href="/w/load.php?lang=en&amp;modules=site.styles&amp;only=styles&amp;skin=vector"/>
<meta name="generator" content="MediaWiki 1.35.0-wmf.31"/>
<meta name="referrer" content="origin"/>
<meta name="referrer" content="origin-when-crossorigin"/>
<meta name="referrer" content="origin-when-cross-origin"/>
<link rel="apple-touch-icon" href="/static/apple-touch/wikipedia.png"/>
<link rel="shortcut icon" href="/static/favicon/wikipedia.ico"/>
<link rel="search" type="application/opensearchdescription+xml" href="/w/opensearch_desc.php" title="Wikipedia (en)"/>
<link rel="EditURI" type="application/rsd+xml" href="//en.wikipedia.org/w/api.php?action=rsd"/>
<link rel="license" href="//creativecommons.org/licenses/by-sa/3.0/"/>
<link rel="alternate" type="application/atom+xml" title="Wikipedia Atom feed" href="/w/index.php?title=Special:RecentChanges&amp;feed=atom"/>
<link rel="canonical" href="https://en.wikipedia.org/wiki/Web_development"/>
<link rel="dns-prefetch" href="//login.wikimedia.org"/>
<link rel="dns-prefetch" href="//meta.wikimedia.org" />
<!--[if lt IE 9]><script src="/w/resources/lib/html5shiv/html5shiv.js"></script><![endif]-->
</head>
<body class="mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-Web_development rootpage-Web_development skin-vector action-view">
<div id="mw-page-base" class="noprint"></div>
<div id="mw-head-base" class="noprint"></div>
<div id="content" class="mw-body" role="main">
	<a id="top"></a>
		<div id="siteNotice" class="mw-body-content"><!-- CentralNotice --></div>
	<div class="mw-indicators mw-body-content">
<div id="mw-indicator-pp-default" class="mw-indicator"><a href="/wiki/Wikipedia:Protection_policy#semi" title="This article is semi-protected."><img alt="Page semi-protected" src="//upload.wikimedia.org/wikipedia/en/thumb/1/1b/Semi-protection-shackle.svg/20px-Semi-protection-shackle.svg.png" decoding="async" width="20" height="20" srcset="//upload.wikimedia.org/wikipedia/en/thumb/1/1b/Semi-protection-shackle.svg/30px-Semi-protection-shackle.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/1/1b/Semi-protection-shackle.svg/40px-Semi-protection-shackle.svg.png 2x" data-file-width="512" data-file-height="512" /></a></div>
</div>

	<h1 id="firstHeading" class="firstHeading" lang="en">Web development</h1>
	
	<div id="bodyContent" class="mw-body-content">
		<div id="siteSub" class="noprint">From Wikipedia, the free encyclopedia</div>
		<div id="contentSub"></div>
		
		
		<div id="jump-to-nav"></div>
		<a class="mw-jump-link" href="#mw-head">Jump to navigation</a>
		<a class="mw-jump-link" href="#p-search">Jump to search</a>
		<div id="mw-content-text" lang="en" dir="ltr" class="mw-content-ltr"><div class="mw-parser-output"><p class="mw-empty-elt">
</p>
<table class="box-More_citations_needed plainlinks metadata ambox ambox-content ambox-Refimprove" role="presentation"><tbody><tr><td class="mbox-image"><div style="width:52px"><a href="/wiki/File:Question_book-new.svg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/50px-Question_book-new.svg.png" decoding="async" width="50" height="39" srcset="//upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/75px-Question_book-new.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/100px-Question_book-new.svg.png 2x" data-file-width="512" data-file-height="399" /></a></div></td><td class="mbox-text"><div class="mbox-text-span">This article <b>needs additional citations for <a href="/wiki/Wikipedia:Verifiability" title="Wikipedia:Verifiability">verification</a></b>.<span class="hide-when-compact"> Please help <a class="external text" href="https://en.wikipedia.org/w/index.php?title=Web_development&amp;action=edit">improve this article</a> by <a href="/wiki/Help:Referencing_for_beginners" title="Help:Referencing for beginners">adding citations to reliable sources</a>. Unsourced material may be challenged and removed.<br /><small><span class="plainlinks"><i>Find sources:</i>&#160;<a rel="nofollow" class="external text" href="//www.google.com/search?as_eq=wikipedia&amp;q=%22Web+development%22">"Web development"</a>&#160;–&#160;<a rel="nofollow" class="external text" href="//www.google.com/search?tbm=nws&amp;q=%22Web+development%22+-wikipedia">news</a>&#160;<b>·</b> <a rel="nofollow" class="external text" href="//www.google.com/search?&amp;q=%22Web+development%22+site:news.google.com/newspapers&amp;source=newspapers">newspapers</a>&#160;<b>·</b> <a rel="nofollow" class="external text" href="//www.google.com/search?tbs=bks:1&amp;q=%22Web+development%22+-wikipedia">books</a>&#160;<b>·</b> <a rel="nofollow" class="external text" href="//scholar.google.com/scholar?q=%22Web+development%22">scholar</a>&#160;<b>·</b> <a rel="nofollow" class="external text" href="https://www.jstor.org/action/doBasicSearch?Query=%22Web+development%22&amp;acc=on&amp;wc=on">JSTOR</a></span></small></span>  <small class="date-container"><i>(<span class="date">December 2012</span>)</i></small><small class="hide-when-compact"><i> (<a href="/wiki/Help:Maintenance_template_removal" title="Help:Maintenance template removal">Learn how and when to remove this template message</a>)</i></small></div></td></tr></tbody></table>
<p><b>Web development</b> is the work involved in developing a <a href="/wiki/Website" title="Website">website</a> for the <a href="/wiki/Internet" title="Internet">Internet</a> (<a href="/wiki/World_Wide_Web" title="World Wide Web">World Wide Web</a>) or an <a href="/wiki/Intranet" title="Intranet">intranet</a> (a private network).<sup id="cite_ref-1" class="reference"><a href="#cite_note-1">&#91;1&#93;</a></sup> Web development can range from developing a simple single <a href="/wiki/Static_web_page" title="Static web page">static page</a> of <a href="/wiki/Plain_text" title="Plain text">plain text</a> to complex web-based <a href="/wiki/Internet_application" class="mw-redirect" title="Internet application">internet applications</a> (web apps), <a href="/wiki/Electronic_business" title="Electronic business">electronic businesses</a>, and <a href="/wiki/Social_network_service" class="mw-redirect" title="Social network service">social network services</a>. A more comprehensive list of tasks to which web development commonly refers, may include <a href="/wiki/Web_engineering" title="Web engineering">web engineering</a>, <a href="/wiki/Web_design" title="Web design">web design</a>, <a href="/wiki/Web_content_development" title="Web content development">web content development</a>, client liaison, <a href="/wiki/Client-side_scripting" class="mw-redirect" title="Client-side scripting">client-side</a>/<a href="/wiki/Server-side_scripting" title="Server-side scripting">server-side</a> <a href="/wiki/Computer_programming" title="Computer programming">scripting</a>, <a href="/wiki/Web_server" title="Web server">web server</a> and <a href="/wiki/Network_security" title="Network security">network security</a> configuration, and <a href="/wiki/E-commerce" title="E-commerce">e-commerce</a> development. 
</p><p>Among web professionals, "web development" usually refers to the main non-design aspects of building websites: writing <a href="/wiki/Markup_language" title="Markup language">markup</a> and <a href="/wiki/Computer_programming" title="Computer programming">coding</a>.<sup id="cite_ref-2" class="reference"><a href="#cite_note-2">&#91;2&#93;</a></sup> Web development may use <a href="/wiki/Content_management_system" title="Content management system">content management systems</a> (CMS) to make content changes easier and available with basic technical skills.
</p><p>For larger organizations and businesses, web development teams can consist of hundreds of people (<a href="/wiki/Web_developer" title="Web developer">web developers</a>) and follow standard methods like <a href="/wiki/Agile_software_development" title="Agile software development">Agile methodologies</a> while developing websites. Smaller organizations may only require a single permanent or contracting developer, or secondary assignment to related job positions such as a <a href="/wiki/Graphic_designer" title="Graphic designer">graphic designer</a> or <a href="/wiki/Information_systems" class="mw-redirect" title="Information systems">information systems</a> technician. Web development may be a collaborative effort between departments rather than the domain of a designated department. There are three kinds of web developer specialization: <a href="/wiki/Front-end_web_development" title="Front-end web development">front-end developer</a>, back-end developer, and <a href="/wiki/Full-stack_developer" class="mw-redirect" title="Full-stack developer">full-stack developer</a>. Front-end developers are responsible for behavior and visuals that run in the user browser, while back-end developers deal with the servers.
</p>
<div id="toc" class="toc" role="navigation" aria-labelledby="mw-toc-heading"><input type="checkbox" role="button" id="toctogglecheckbox" class="toctogglecheckbox" style="display:none" /><div class="toctitle" lang="en" dir="ltr"><h2 id="mw-toc-heading">Contents</h2><span class="toctogglespan"><label class="toctogglelabel" for="toctogglecheckbox"></label></span></div>
<ul>
<li class="toclevel-1 tocsection-1"><a href="#As_an_industry"><span class="tocnumber">1</span> <span class="toctext">As an industry</span></a></li>
<li class="toclevel-1 tocsection-2"><a href="#Chronology"><span class="tocnumber">2</span> <span class="toctext">Chronology</span></a></li>
<li class="toclevel-1 tocsection-3"><a href="#Practical_web_development"><span class="tocnumber">3</span> <span class="toctext">Practical web development</span></a>
<ul>
<li class="toclevel-2 tocsection-4"><a href="#Basic"><span class="tocnumber">3.1</span> <span class="toctext">Basic</span></a></li>
<li class="toclevel-2 tocsection-5"><a href="#Testing"><span class="tocnumber">3.2</span> <span class="toctext">Testing</span></a></li>
</ul>
</li>
<li class="toclevel-1 tocsection-6"><a href="#Security_considerations"><span class="tocnumber">4</span> <span class="toctext">Security considerations</span></a></li>
<li class="toclevel-1 tocsection-7"><a href="#See_also"><span class="tocnumber">5</span> <span class="toctext">See also</span></a></li>
<li class="toclevel-1 tocsection-8"><a href="#References"><span class="tocnumber">6</span> <span class="toctext">References</span></a></li>
</ul>
</div>

<h2><span class="mw-headline" id="As_an_industry">As an industry</span></h2>
<table class="box-Essay-like plainlinks metadata ambox ambox-style ambox-essay-like" role="presentation"><tbody><tr><td class="mbox-image"><div style="width:52px"><img alt="" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/40px-Edit-clear.svg.png" decoding="async" width="40" height="40" srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/60px-Edit-clear.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/80px-Edit-clear.svg.png 2x" data-file-width="48" data-file-height="48" /></div></td><td class="mbox-text"><div class="mbox-text-span">This section <b>is written like a <a href="/wiki/Wikipedia:What_Wikipedia_is_not#Wikipedia_is_not_a_publisher_of_original_thought" title="Wikipedia:What Wikipedia is not">personal reflection, personal essay, or argumentative essay</a></b> that states a Wikipedia editor's personal feelings or presents an original argument about a topic.<span class="hide-when-compact"> Please <a class="external text" href="https://en.wikipedia.org/w/index.php?title=Web_development&amp;action=edit">help improve it</a> by rewriting it in an <a href="/wiki/Wikipedia:Writing_better_articles#Information_style_and_tone" title="Wikipedia:Writing better articles">encyclopedic style</a>.</span>  <small class="date-container"><i>(<span class="date">September 2018</span>)</i></small><small class="hide-when-compact"><i> (<a href="/wiki/Help:Maintenance_template_removal" title="Help:Maintenance template removal">Learn how and when to remove this template message</a>)</i></small></div></td></tr></tbody></table>
<p>Since the <a href="/wiki/History_of_the_World_Wide_Web#1996–1998:_Commercialization_of_the_WWW" title="History of the World Wide Web">commercialization of the web</a>, web development has been a growing <a href="/wiki/Industry" title="Industry">industry</a>. The growth of this industry is being driven by businesses wishing to use their website to advertise and sell products and services to customers.<sup id="cite_ref-3" class="reference"><a href="#cite_note-3">&#91;3&#93;</a></sup>
</p><p>There are many <a href="/wiki/Open_source" title="Open source">open source</a> tools for web development such as <a href="/wiki/Berkeley_DB" title="Berkeley DB">BerkeleyDB</a>, <a href="/wiki/GlassFish" title="GlassFish">GlassFish</a>, <a href="/wiki/LAMP_(software_bundle)" title="LAMP (software bundle)">LAMP</a> (<a href="/wiki/Linux" title="Linux">Linux</a>, <a href="/wiki/Apache_HTTP_Server" title="Apache HTTP Server">Apache</a>, <a href="/wiki/MySQL" title="MySQL">MySQL</a>, <a href="/wiki/PHP" title="PHP">PHP</a>) stack and <a href="/wiki/Plack_(software)" title="Plack (software)">Perl/Plack</a>. This has kept the cost of learning web development to a minimum. Another contributing factor to the growth of the industry has been the rise of easy-to-use <a href="/wiki/WYSIWYG" title="WYSIWYG">WYSIWYG</a> web-development software, such as <a href="/wiki/Adobe_Dreamweaver" title="Adobe Dreamweaver">Adobe Dreamweaver</a>, <a href="/wiki/BlueGriffon" title="BlueGriffon">BlueGriffon</a> and <a href="/wiki/Microsoft_Visual_Studio" title="Microsoft Visual Studio">Microsoft Visual Studio</a>. Knowledge of <a href="/wiki/HTML" title="HTML">HyperText Markup Language</a> (HTML) or of programming languages is still required to use such software, but the basics can be learned and implemented quickly.
</p><p>An ever-growing set of tools and technologies have helped developers build more dynamic and interactive websites. Further, web developers now help to deliver applications as web services which were traditionally only available as applications on a desk-based computer. This has allowed for many opportunities to decentralize information and media distribution. Examples can be seen with the rise of <a href="/wiki/Cloud_computing" title="Cloud computing">cloud</a> services such as <a href="/wiki/Adobe_Creative_Cloud" title="Adobe Creative Cloud">Adobe Creative Cloud</a>, <a href="/wiki/Dropbox_(service)" title="Dropbox (service)">Dropbox</a> and <a href="/wiki/Google_Drive" title="Google Drive">Google Drive</a>. These web services allow users to interact with applications from many locations, instead of being tied to a specific workstation for their application environment.
</p><p>Examples of dramatic transformation in communication and commerce led by web development include e-commerce. Online auction sites such as <a href="/wiki/EBay" title="EBay">eBay</a> have changed the way consumers find and purchase goods and services. Online retailers such as <a href="/wiki/Amazon.com" class="mw-redirect" title="Amazon.com">Amazon.com</a> and <a href="/wiki/Buy.com" class="mw-redirect" title="Buy.com">Buy.com</a> (among many others) have transformed the shopping and bargain-hunting experience for many consumers. Another example of transformative communication led by web development is the <a href="/wiki/Blog" title="Blog">blog</a>. Web applications such as <a href="/wiki/WordPress" title="WordPress">WordPress</a> and <a href="/wiki/Movable_Type" title="Movable Type">Movable Type</a> have created blog-environments for individual websites. The increased usage of open-source <a href="/wiki/Content_management_systems" class="mw-redirect" title="Content management systems">content management systems</a> and <a href="/wiki/Enterprise_content_management" title="Enterprise content management">enterprise content management</a> systems has extended web development's impact at online interaction and communication.
</p><p>Web development has also impacted personal networking and marketing. Websites are no longer simply tools for work or for <a href="/wiki/Commerce" title="Commerce">commerce</a>, but serve more broadly for communication and <a href="/wiki/Social_networking" class="mw-redirect" title="Social networking">social networking</a>. Web sites such as <a href="/wiki/Facebook" title="Facebook">Facebook</a> and <a href="/wiki/Twitter" title="Twitter">Twitter</a> provide users with a platform to communicate and organizations with a more personal and interactive way to engage the public.
</p>
<h2><span class="mw-headline" id="Chronology">Chronology</span></h2>
<p><a href="/wiki/File:Webdevelopmenttimeline.png" class="image"><img alt="Webdevelopmenttimeline.png" src="//upload.wikimedia.org/wikipedia/commons/e/e8/Webdevelopmenttimeline.png" decoding="async" width="800" height="664" data-file-width="800" data-file-height="664" /></a>
</p>
<h2><span class="mw-headline" id="Practical_web_development">Practical web development</span></h2>
<h3><span class="mw-headline" id="Basic">Basic</span></h3>
<p>In practice, many <a href="/wiki/Web_developer" title="Web developer">web developers</a> will have basic <b>interdisciplinary</b> skills / roles, including:
</p>
<ul><li><a href="/wiki/Graphic_design" title="Graphic design">Graphic design</a> / <a href="/wiki/Web_design" title="Web design">web design</a></li>
<li><a href="/wiki/Information_architecture" title="Information architecture">Information architecture</a> and <a href="/wiki/Copywriting" title="Copywriting">copywriting</a>/<a href="/wiki/Copyediting" class="mw-redirect" title="Copyediting">copyediting</a> with web <a href="/wiki/Usability" title="Usability">usability</a>, <a href="/wiki/Web_accessibility" title="Web accessibility">accessibility</a> and <a href="/wiki/Search_engine_optimization" title="Search engine optimization">search engine optimization</a> in mind</li>
<li>Mobile responsiveness</li></ul>
<h3><span class="mw-headline" id="Testing">Testing</span></h3>
<div role="note" class="hatnote navigation-not-searchable">Main article: <a href="/wiki/Software_testing" title="Software testing">Software testing</a></div>
<p>Testing is the process of evaluating a system or its component(s) with the intent to find whether it satisfies the specified requirements or not. Testing is executing a system in order to identify any gaps, errors, or missing requirements contrary to the actual requirements.
The extent of testing varies greatly between organizations, developers, and individual sites or applications.
</p>
<h2><span class="mw-headline" id="Security_considerations">Security considerations</span></h2>
<p><i>Web development</i> takes into account many security considerations, such as data entry error checking through forms, filtering output, and encryption. Malicious practices such as <a href="/wiki/SQL_injection" title="SQL injection">SQL injection</a> can be executed by users with ill intent yet with only primitive knowledge of web development as a whole. Scripts can be used to exploit websites by granting unauthorized access to malicious users that try to collect information such as email addresses, passwords and protected content like credit card numbers.
</p><p>Some of this is dependent on the server environment on which the scripting language, such as <a href="/wiki/Active_Server_Pages" title="Active Server Pages">ASP</a>, <a href="/wiki/JavaServer_Pages" title="JavaServer Pages">JSP</a>, <a href="/wiki/PHP" title="PHP">PHP</a>, <a href="/wiki/Python_(programming_language)" title="Python (programming language)">Python</a>, <a href="/wiki/Perl" title="Perl">Perl</a> or <a href="/wiki/Ruby_(programming_language)" title="Ruby (programming language)">Ruby</a> is running, and therefore is not necessarily down to the web developer themselves to maintain. However, stringent testing of web applications before public release is encouraged to prevent such exploits from occurring.
If some contact form is provided on a website it should include a captcha field in it which prevents computer programs from automatically filling forms and also mail spamming.
</p><p>Keeping a web server safe from intrusion is often called <i>Server Port Hardening</i>. Many technologies come into play to keep information on the internet safe when it is transmitted from one location to another. For instance <a href="/wiki/Transport_Layer_Security" title="Transport Layer Security">TLS certificates</a> (or "SSL certificates") are issued by certificate authorities to help prevent <a href="/wiki/Internet_fraud" title="Internet fraud">internet fraud</a>. Many developers often employ different forms of <a href="/wiki/Encryption" title="Encryption">encryption</a> when transmitting and storing sensitive information. A basic understanding of <a href="/wiki/Information_technology" title="Information technology">information technology</a> security concerns is often part of a web developer's knowledge.
</p><p>Because new security holes are found in web applications even after testing and launch, security patch updates are frequent for widely used applications. It is often the job of web developers to keep applications up to date as security patches are released and new security concerns are discovered.
</p>
<h2><span class="mw-headline" id="See_also">See also</span></h2>
<ul><li><a href="/wiki/Outline_of_web_design_and_web_development" title="Outline of web design and web development">Outline of web design and web development</a></li>
<li><a href="/wiki/Web_design" title="Web design">Web design</a></li>
<li><a href="/wiki/Web_development_tools" title="Web development tools">Web development tools</a></li>
<li><a href="/wiki/Web_application_development" title="Web application development">Web application development</a></li>
<li><a href="/wiki/Web_developer" title="Web developer">Web developer</a></li>
<li><a href="/wiki/Internet" title="Internet">Internet</a></li>
<li><a href="/wiki/Intranet" title="Intranet">Intranet</a></li></ul>
<h2><span class="mw-headline" id="References">References</span></h2>
<div class="reflist" style="list-style-type: decimal;">
<div class="mw-references-wrap"><ol class="references">
<li id="cite_note-1"><span class="mw-cite-backlink"><b><a href="#cite_ref-1">^</a></b></span> <span class="reference-text"><cite class="citation web"><a rel="nofollow" class="external text" href="https://www.techopedia.com/definition/23889/web-development">"What is Web Development? - Definition from Techopedia"</a>. <i>Techopedia.com</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2018-12-07</span></span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Techopedia.com&amp;rft.atitle=What+is+Web+Development%3F+-+Definition+from+Techopedia&amp;rft_id=https%3A%2F%2Fwww.techopedia.com%2Fdefinition%2F23889%2Fweb-development&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AWeb+development" class="Z3988"></span><style data-mw-deduplicate="TemplateStyles:r951705291">.mw-parser-output cite.citation{font-style:inherit}.mw-parser-output .citation q{quotes:"\"""\"""'""'"}.mw-parser-output .id-lock-free a,.mw-parser-output .citation .cs1-lock-free a{background-image:url("//upload.wikimedia.org/wikipedia/commons/thumb/6/65/Lock-green.svg/9px-Lock-green.svg.png");background-image:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/6/65/Lock-green.svg");background-repeat:no-repeat;background-size:9px;background-position:right .1em center}.mw-parser-output .id-lock-limited a,.mw-parser-output .id-lock-registration a,.mw-parser-output .citation .cs1-lock-limited a,.mw-parser-output .citation .cs1-lock-registration a{background-image:url("//upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Lock-gray-alt-2.svg/9px-Lock-gray-alt-2.svg.png");background-image:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/d/d6/Lock-gray-alt-2.svg");background-repeat:no-repeat;background-size:9px;background-position:right .1em center}.mw-parser-output .id-lock-subscription a,.mw-parser-output .citation .cs1-lock-subscription a{background-image:url("//upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Lock-red-alt-2.svg/9px-Lock-red-alt-2.svg.png");background-image:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/a/aa/Lock-red-alt-2.svg");background-repeat:no-repeat;background-size:9px;background-position:right .1em center}.mw-parser-output .cs1-subscription,.mw-parser-output .cs1-registration{color:#555}.mw-parser-output .cs1-subscription span,.mw-parser-output .cs1-registration span{border-bottom:1px dotted;cursor:help}.mw-parser-output .cs1-ws-icon a{background-image:url("//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/12px-Wikisource-logo.svg.png");background-image:linear-gradient(transparent,transparent),url("//upload.wikimedia.org/wikipedia/commons/4/4c/Wikisource-logo.svg");background-repeat:no-repeat;background-size:12px;background-position:right .1em center}.mw-parser-output code.cs1-code{color:inherit;background:inherit;border:inherit;padding:inherit}.mw-parser-output .cs1-hidden-error{display:none;font-size:100%}.mw-parser-output .cs1-visible-error{font-size:100%}.mw-parser-output .cs1-maint{display:none;color:#33aa33;margin-left:0.3em}.mw-parser-output .cs1-subscription,.mw-parser-output .cs1-registration,.mw-parser-output .cs1-format{font-size:95%}.mw-parser-output .cs1-kern-left,.mw-parser-output .cs1-kern-wl-left{padding-left:0.2em}.mw-parser-output .cs1-kern-right,.mw-parser-output .cs1-kern-wl-right{padding-right:0.2em}.mw-parser-output .citation .mw-selflink{font-weight:inherit}</style></span>
</li>
<li id="cite_note-2"><span class="mw-cite-backlink"><b><a href="#cite_ref-2">^</a></b></span> <span class="reference-text"><cite id="CITEREFCampbell2017" class="citation book">Campbell, Jennifer (2017). <i>Web Design: Introductory</i>. Cengage Learning. p.&#160;27.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&amp;rft.genre=book&amp;rft.btitle=Web+Design%3A+Introductory&amp;rft.pages=27&amp;rft.pub=Cengage+Learning&amp;rft.date=2017&amp;rft.aulast=Campbell&amp;rft.aufirst=Jennifer&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AWeb+development" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
<li id="cite_note-3"><span class="mw-cite-backlink"><b><a href="#cite_ref-3">^</a></b></span> <span class="reference-text"><cite id="CITEREFBureau_of_Labor_Statistics,_U.S._Department_of_Labor" class="citation web">Bureau of Labor Statistics, U.S. Department of Labor. <a rel="nofollow" class="external text" href="http://www.bls.gov/oes/2011/may/oes151179.htm">"Information Security Analysts, Web Developers, and Computer Network Architects"</a>. <i>Occupational Outlook Handbook, 2012-13 Edition</i><span class="reference-accessdate">. Retrieved <span class="nowrap">2013-01-17</span></span>.</cite><span title="ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=unknown&amp;rft.jtitle=Occupational+Outlook+Handbook%2C+2012-13+Edition&amp;rft.atitle=Information+Security+Analysts%2C+Web+Developers%2C+and+Computer+Network+Architects&amp;rft.au=Bureau+of+Labor+Statistics%2C+U.S.+Department+of+Labor&amp;rft_id=http%3A%2F%2Fwww.bls.gov%2Foes%2F2011%2Fmay%2Foes151179.htm&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AWeb+development" class="Z3988"></span><link rel="mw-deduplicated-inline-style" href="mw-data:TemplateStyles:r951705291"/></span>
</li>
</ol></div></div>
<div role="navigation" class="navbox authority-control" aria-labelledby="Authority_control_frameless_&amp;#124;text-top_&amp;#124;10px_&amp;#124;alt=Edit_this_at_Wikidata_&amp;#124;link=https&amp;#58;//www.wikidata.org/wiki/Q386275&amp;#124;Edit_this_at_Wikidata" style="padding:3px"><table class="nowraplinks hlist navbox-inner" style="border-spacing:0;background:transparent;color:inherit"><tbody><tr><th id="Authority_control_frameless_&amp;#124;text-top_&amp;#124;10px_&amp;#124;alt=Edit_this_at_Wikidata_&amp;#124;link=https&amp;#58;//www.wikidata.org/wiki/Q386275&amp;#124;Edit_this_at_Wikidata" scope="row" class="navbox-group" style="width:1%"><a href="/wiki/Help:Authority_control" title="Help:Authority control">Authority control</a> <a href="https://www.wikidata.org/wiki/Q386275" title="Edit this at Wikidata"><img alt="Edit this at Wikidata" src="//upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/10px-OOjs_UI_icon_edit-ltr-progressive.svg.png" decoding="async" width="10" height="10" style="vertical-align: text-top" srcset="//upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/15px-OOjs_UI_icon_edit-ltr-progressive.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/20px-OOjs_UI_icon_edit-ltr-progressive.svg.png 2x" data-file-width="20" data-file-height="20" /></a></th><td class="navbox-list navbox-odd" style="text-align:left;border-left-width:2px;border-left-style:solid;width:100%;padding:0px"><div style="padding:0em 0.25em">
<ul><li><span class="nowrap"><a href="/wiki/LCCN_(identifier)" class="mw-redirect" title="LCCN (identifier)">LCCN</a>: <span class="uid"><a rel="nofollow" class="external text" href="https://id.loc.gov/authorities/subjects/sh98004795">sh98004795</a></span></span></li></ul>
</div></td></tr></tbody></table></div>
<!-- 
NewPP limit report
Parsed by mw1366
Cached time: 20200516045241
Cache expiry: 2592000
Dynamic content: false
Complications: [vary‐revision‐sha1]
CPU time usage: 0.276 seconds
Real time usage: 0.422 seconds
Preprocessor visited node count: 540/1000000
Post‐expand include size: 20809/2097152 bytes
Template argument size: 396/2097152 bytes
Highest expansion depth: 13/40
Expensive parser function count: 6/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 11362/5000000 bytes
Number of Wikibase entities loaded: 1/400
Lua time usage: 0.172/10.000 seconds
Lua memory usage: 3.61 MB/50 MB
-->
<!--
Transclusion expansion time report (%,ms,calls,template)
100.00%  380.920      1 -total
 29.73%  113.239      1 Template:Reflist
 25.30%   96.374      1 Template:Refimprove
 24.15%   91.977      2 Template:Cite_web
 23.64%   90.041      2 Template:Ambox
 18.91%   72.034      1 Template:Pp-semi
 13.41%   51.085      1 Template:Authority_control
 10.56%   40.215      1 Template:Find_sources_mainspace
  7.49%   28.536      1 Template:Essay-like
  5.10%   19.432      1 Template:DMCA
-->

<!-- Saved in parser cache with key enwiki:pcache:idhash:611714-0!canonical and timestamp 20200516045240 and revision id 940071839
 -->
</div><noscript><img src="//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1" alt="" title="" width="1" height="1" style="border: none; position: absolute;" /></noscript></div>
		<div class="printfooter">Retrieved from "<a dir="ltr" href="https://en.wikipedia.org/w/index.php?title=Web_development&amp;oldid=940071839">https://en.wikipedia.org/w/index.php?title=Web_development&amp;oldid=940071839</a>"</div>
		<div id="catlinks" class="catlinks" data-mw="interface"><div id="mw-normal-catlinks" class="mw-normal-catlinks"><a href="/wiki/Help:Category" title="Help:Category">Categories</a>: <ul><li><a href="/wiki/Category:Web_development" title="Category:Web development">Web development</a></li></ul></div><div id="mw-hidden-catlinks" class="mw-hidden-catlinks mw-hidden-cats-hidden">Hidden categories: <ul><li><a href="/wiki/Category:Wikipedia_indefinitely_semi-protected_pages" title="Category:Wikipedia indefinitely semi-protected pages">Wikipedia indefinitely semi-protected pages</a></li><li><a href="/wiki/Category:Articles_needing_additional_references_from_December_2012" title="Category:Articles needing additional references from December 2012">Articles needing additional references from December 2012</a></li><li><a href="/wiki/Category:All_articles_needing_additional_references" title="Category:All articles needing additional references">All articles needing additional references</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_style_issues_from_September_2018" title="Category:Wikipedia articles with style issues from September 2018">Wikipedia articles with style issues from September 2018</a></li><li><a href="/wiki/Category:All_articles_with_style_issues" title="Category:All articles with style issues">All articles with style issues</a></li><li><a href="/wiki/Category:Wikipedia_articles_with_LCCN_identifiers" title="Category:Wikipedia articles with LCCN identifiers">Wikipedia articles with LCCN identifiers</a></li></ul></div></div>
		<div class="visualClear"></div>
		
	</div>
</div>
<div id='mw-data-after-content'>
	<div class="read-more-container"></div>
</div>

<div id="mw-navigation">
	<h2>Navigation menu</h2>
	<div id="mw-head">
		
<div id="p-personal" role="navigation" class="" aria-labelledby="p-personal-label">
	<h3 id="p-personal-label">Personal tools</h3>
	<ul >
		<li id="pt-anonuserpage">Not logged in</li><li id="pt-anontalk"><a href="/wiki/Special:MyTalk" title="Discussion about edits from this IP address [n]" accesskey="n">Talk</a></li><li id="pt-anoncontribs"><a href="/wiki/Special:MyContributions" title="A list of edits made from this IP address [y]" accesskey="y">Contributions</a></li><li id="pt-createaccount"><a href="/w/index.php?title=Special:CreateAccount&amp;returnto=Web+development" title="You are encouraged to create an account and log in; however, it is not mandatory">Create account</a></li><li id="pt-login"><a href="/w/index.php?title=Special:UserLogin&amp;returnto=Web+development" title="You&#039;re encouraged to log in; however, it&#039;s not mandatory. [o]" accesskey="o">Log in</a></li>
	</ul>
</div>

		<div id="left-navigation">
			<div id="p-namespaces" role="navigation" class="vectorTabs" aria-labelledby="p-namespaces-label">
	<h3 id="p-namespaces-label">Namespaces</h3>
	<ul >
		<li id="ca-nstab-main" class="selected"><a href="/wiki/Web_development" title="View the content page [c]" accesskey="c">Article</a></li><li id="ca-talk"><a href="/wiki/Talk:Web_development" rel="discussion" title="Discuss improvements to the content page [t]" accesskey="t">Talk</a></li>
	</ul>
</div>

			<div id="p-variants" role="navigation" class="emptyPortlet vectorMenu" aria-labelledby="p-variants-label">
	<input type="checkbox" class="vectorMenuCheckbox" aria-labelledby="p-variants-label" />
	<h3 id="p-variants-label">
		<span>Variants</span>
	</h3>
	<ul class="menu" >
		
	</ul>
</div>

		</div>
		<div id="right-navigation">
			<div id="p-views" role="navigation" class="vectorTabs" aria-labelledby="p-views-label">
	<h3 id="p-views-label">Views</h3>
	<ul >
		<li id="ca-view" class="collapsible selected"><a href="/wiki/Web_development">Read</a></li><li id="ca-viewsource" class="collapsible"><a href="/w/index.php?title=Web_development&amp;action=edit" title="This page is protected.&#10;You can view its source [e]" accesskey="e">View source</a></li><li id="ca-history" class="collapsible"><a href="/w/index.php?title=Web_development&amp;action=history" title="Past revisions of this page [h]" accesskey="h">View history</a></li>
	</ul>
</div>

			<div id="p-cactions" role="navigation" class="emptyPortlet vectorMenu" aria-labelledby="p-cactions-label">
	<input type="checkbox" class="vectorMenuCheckbox" aria-labelledby="p-cactions-label" />
	<h3 id="p-cactions-label">
		<span>More</span>
	</h3>
	<ul class="menu" >
		
	</ul>
</div>

			<div id="p-search" role="search">
	<h3 >
		<label for="searchInput">Search</label>
	</h3>
	<form action="/w/index.php" id="searchform">
		<div id="simpleSearch">
			<input type="search" name="search" placeholder="Search Wikipedia" title="Search Wikipedia [f]" accesskey="f" id="searchInput"/>
			<input type="hidden" value="Special:Search" name="title"/>
			<input type="submit" name="fulltext" value="Search" title="Search Wikipedia for this text" id="mw-searchButton" class="searchButton mw-fallbackSearchButton"/>
			<input type="submit" name="go" value="Go" title="Go to a page with this exact name if it exists" id="searchButton" class="searchButton"/>
		</div>
	</form>
</div>

		</div>
	</div>
	
<div id="mw-panel">
	<div id="p-logo" role="banner">
		<a  title="Visit the main page" class="mw-wiki-logo" href="/wiki/Main_Page"></a>
	</div>
	<div class="portal portal-first" role="navigation" id="p-navigation"  aria-labelledby="p-navigation-label">
	<h3  id="p-navigation-label">
		Navigation
	</h3>
	<div class="body">
		<ul><li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li><li id="n-contents"><a href="/wiki/Wikipedia:Contents" title="Guides to browsing Wikipedia">Contents</a></li><li id="n-featuredcontent"><a href="/wiki/Wikipedia:Featured_content" title="Featured content – the best of Wikipedia">Featured content</a></li><li id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Find background information on current events">Current events</a></li><li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random article [x]" accesskey="x">Random article</a></li><li id="n-sitesupport"><a href="https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wikipedia.org&amp;uselang=en" title="Support us">Donate to Wikipedia</a></li><li id="n-shoplink"><a href="//shop.wikimedia.org" title="Visit the Wikipedia store">Wikipedia store</a></li></ul>
		
	</div>
</div>


	<div class="portal" role="navigation" id="p-interaction"  aria-labelledby="p-interaction-label">
	<h3  id="p-interaction-label">
		Interaction
	</h3>
	<div class="body">
		<ul><li id="n-help"><a href="/wiki/Help:Contents" title="Guidance on how to use and edit Wikipedia">Help</a></li><li id="n-aboutsite"><a href="/wiki/Wikipedia:About" title="Find out about Wikipedia">About Wikipedia</a></li><li id="n-portal"><a href="/wiki/Wikipedia:Community_portal" title="About the project, what you can do, where to find things">Community portal</a></li><li id="n-recentchanges"><a href="/wiki/Special:RecentChanges" title="A list of recent changes in the wiki [r]" accesskey="r">Recent changes</a></li><li id="n-contactpage"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us" title="How to contact Wikipedia">Contact page</a></li></ul>
		
	</div>
</div>

<div class="portal" role="navigation" id="p-tb"  aria-labelledby="p-tb-label">
	<h3  id="p-tb-label">
		Tools
	</h3>
	<div class="body">
		<ul><li id="t-whatlinkshere"><a href="/wiki/Special:WhatLinksHere/Web_development" title="List of all English Wikipedia pages containing links to this page [j]" accesskey="j">What links here</a></li><li id="t-recentchangeslinked"><a href="/wiki/Special:RecentChangesLinked/Web_development" rel="nofollow" title="Recent changes in pages linked from this page [k]" accesskey="k">Related changes</a></li><li id="t-upload"><a href="/wiki/Wikipedia:File_Upload_Wizard" title="Upload files [u]" accesskey="u">Upload file</a></li><li id="t-specialpages"><a href="/wiki/Special:SpecialPages" title="A list of all special pages [q]" accesskey="q">Special pages</a></li><li id="t-permalink"><a href="/w/index.php?title=Web_development&amp;oldid=940071839" title="Permanent link to this revision of the page">Permanent link</a></li><li id="t-info"><a href="/w/index.php?title=Web_development&amp;action=info" title="More information about this page">Page information</a></li><li id="t-wikibase"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q386275" title="Link to connected data repository item [g]" accesskey="g">Wikidata item</a></li><li id="t-cite"><a href="/w/index.php?title=Special:CiteThisPage&amp;page=Web_development&amp;id=940071839&amp;wpFormIdentifier=titleform" title="Information on how to cite this page">Cite this page</a></li></ul>
		
	</div>
</div>

<div class="portal" role="navigation" id="p-wikibase-otherprojects"  aria-labelledby="p-wikibase-otherprojects-label">
	<h3  id="p-wikibase-otherprojects-label">
		In other projects
	</h3>
	<div class="body">
		<ul><li class="wb-otherproject-link wb-otherproject-commons"><a href="https://commons.wikimedia.org/wiki/Category:Web_development" hreflang="en">Wikimedia Commons</a></li><li class="wb-otherproject-link wb-otherproject-wikibooks"><a href="https://en.wikibooks.org/wiki/Web_Development" hreflang="en">Wikibooks</a></li></ul>
		
	</div>
</div>

<div class="portal" role="navigation" id="p-coll-print_export"  aria-labelledby="p-coll-print_export-label">
	<h3  id="p-coll-print_export-label">
		Print/export
	</h3>
	<div class="body">
		<ul><li id="coll-download-as-rl"><a href="/w/index.php?title=Special:ElectronPdf&amp;page=Web+development&amp;action=show-download-screen">Download as PDF</a></li><li id="t-print"><a href="/w/index.php?title=Web_development&amp;printable=yes" title="Printable version of this page [p]" accesskey="p">Printable version</a></li></ul>
		
	</div>
</div>

<div class="portal" role="navigation" id="p-lang"  aria-labelledby="p-lang-label">
	<h3  id="p-lang-label">
		Languages
	</h3>
	<div class="body">
		<ul><li class="interlanguage-link interwiki-ar"><a href="https://ar.wikipedia.org/wiki/%D8%AA%D8%B7%D9%88%D9%8A%D8%B1_%D9%88%D9%8A%D8%A8" title="تطوير ويب – Arabic" lang="ar" hreflang="ar" class="interlanguage-link-target">العربية</a></li><li class="interlanguage-link interwiki-bn"><a href="https://bn.wikipedia.org/wiki/%E0%A6%93%E0%A6%AF%E0%A6%BC%E0%A7%87%E0%A6%AC_%E0%A6%A1%E0%A7%87%E0%A6%AD%E0%A7%87%E0%A6%B2%E0%A6%AA%E0%A6%AE%E0%A7%87%E0%A6%A8%E0%A7%8D%E0%A6%9F" title="ওয়েব ডেভেলপমেন্ট – Bangla" lang="bn" hreflang="bn" class="interlanguage-link-target">বাংলা</a></li><li class="interlanguage-link interwiki-bg"><a href="https://bg.wikipedia.org/wiki/%D0%A3%D0%B5%D0%B1_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%B8%D1%80%D0%B0%D0%BD%D0%B5" title="Уеб програмиране – Bulgarian" lang="bg" hreflang="bg" class="interlanguage-link-target">Български</a></li><li class="interlanguage-link interwiki-de"><a href="https://de.wikipedia.org/wiki/Webentwicklung" title="Webentwicklung – German" lang="de" hreflang="de" class="interlanguage-link-target">Deutsch</a></li><li class="interlanguage-link interwiki-es"><a href="https://es.wikipedia.org/wiki/Desarrollo_web" title="Desarrollo web – Spanish" lang="es" hreflang="es" class="interlanguage-link-target">Español</a></li><li class="interlanguage-link interwiki-fa"><a href="https://fa.wikipedia.org/wiki/%D8%AA%D9%88%D8%B3%D8%B9%D9%87_%D9%88%D8%A8" title="توسعه وب – Persian" lang="fa" hreflang="fa" class="interlanguage-link-target">فارسی</a></li><li class="interlanguage-link interwiki-fr"><a href="https://fr.wikipedia.org/wiki/Programmation_web" title="Programmation web – French" lang="fr" hreflang="fr" class="interlanguage-link-target">Français</a></li><li class="interlanguage-link interwiki-ko"><a href="https://ko.wikipedia.org/wiki/%EC%9B%B9_%EA%B0%9C%EB%B0%9C" title="웹 개발 – Korean" lang="ko" hreflang="ko" class="interlanguage-link-target">한국어</a></li><li class="interlanguage-link interwiki-hy"><a href="https://hy.wikipedia.org/wiki/%D5%8E%D5%A5%D5%A2_%D5%AE%D6%80%D5%A1%D5%A3%D6%80%D5%A1%D5%BE%D5%B8%D6%80%D5%B8%D6%82%D5%B4" title="Վեբ ծրագրավորում – Armenian" lang="hy" hreflang="hy" class="interlanguage-link-target">Հայերեն</a></li><li class="interlanguage-link interwiki-id"><a href="https://id.wikipedia.org/wiki/Pengembangan_web" title="Pengembangan web – Indonesian" lang="id" hreflang="id" class="interlanguage-link-target">Bahasa Indonesia</a></li><li class="interlanguage-link interwiki-ku"><a href="https://ku.wikipedia.org/wiki/P%C3%AA%C5%9Fvebirina_Web%C3%AA" title="Pêşvebirina Webê – Kurdish" lang="ku" hreflang="ku" class="interlanguage-link-target">Kurdî</a></li><li class="interlanguage-link interwiki-lv"><a href="https://lv.wikipedia.org/wiki/T%C4%ABmek%C4%BCa_izstr%C4%81de" title="Tīmekļa izstrāde – Latvian" lang="lv" hreflang="lv" class="interlanguage-link-target">Latviešu</a></li><li class="interlanguage-link interwiki-ml"><a href="https://ml.wikipedia.org/wiki/%E0%B4%B5%E0%B5%86%E0%B4%AC%E0%B5%8D_%E0%B4%A1%E0%B4%B5%E0%B4%B2%E0%B4%AA%E0%B5%8D%E2%80%8D%E0%B4%AE%E0%B5%86%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%8D" title="വെബ് ഡവലപ്‍മെന്റ് – Malayalam" lang="ml" hreflang="ml" class="interlanguage-link-target">മലയാളം</a></li><li class="interlanguage-link interwiki-nl"><a href="https://nl.wikipedia.org/wiki/Webdevelopment" title="Webdevelopment – Dutch" lang="nl" hreflang="nl" class="interlanguage-link-target">Nederlands</a></li><li class="interlanguage-link interwiki-ja"><a href="https://ja.wikipedia.org/wiki/Web%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0" title="Webプログラミング – Japanese" lang="ja" hreflang="ja" class="interlanguage-link-target">日本語</a></li><li class="interlanguage-link interwiki-pt"><a href="https://pt.wikipedia.org/wiki/Desenvolvimento_web" title="Desenvolvimento web – Portuguese" lang="pt" hreflang="pt" class="interlanguage-link-target">Português</a></li><li class="interlanguage-link interwiki-ro"><a href="https://ro.wikipedia.org/wiki/Dezvoltare_web" title="Dezvoltare web – Romanian" lang="ro" hreflang="ro" class="interlanguage-link-target">Română</a></li><li class="interlanguage-link interwiki-ru"><a href="https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D0%B1-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5" title="Веб-программирование – Russian" lang="ru" hreflang="ru" class="interlanguage-link-target">Русский</a></li><li class="interlanguage-link interwiki-sr"><a href="https://sr.wikipedia.org/wiki/Veb-razvoj" title="Veb-razvoj – Serbian" lang="sr" hreflang="sr" class="interlanguage-link-target">Српски / srpski</a></li><li class="interlanguage-link interwiki-sv"><a href="https://sv.wikipedia.org/wiki/Webbutveckling" title="Webbutveckling – Swedish" lang="sv" hreflang="sv" class="interlanguage-link-target">Svenska</a></li><li class="interlanguage-link interwiki-uk"><a href="https://uk.wikipedia.org/wiki/%D0%92%D0%B5%D0%B1%D1%80%D0%BE%D0%B7%D1%80%D0%BE%D0%B1%D0%BA%D0%B0" title="Веброзробка – Ukrainian" lang="uk" hreflang="uk" class="interlanguage-link-target">Українська</a></li><li class="interlanguage-link interwiki-zh"><a href="https://zh.wikipedia.org/wiki/%E7%B6%B2%E9%A0%81%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88" title="網頁程式設計 – Chinese" lang="zh" hreflang="zh" class="interlanguage-link-target">中文</a></li></ul>
		<div class="after-portlet after-portlet-lang"><span class="wb-langlinks-edit wb-langlinks-link"><a href="https://www.wikidata.org/wiki/Special:EntityPage/Q386275#sitelinks-wikipedia" title="Edit interlanguage links" class="wbc-editpage">Edit links</a></span></div>
	</div>
</div>


</div>

</div>

<div id="footer" class="mw-footer" role="contentinfo" >
	<ul id="footer-info" >
		<li id="footer-info-lastmod"> This page was last edited on 10 February 2020, at 10:52<span class="anonymous-show">&#160;(UTC)</span>.</li>
		<li id="footer-info-copyright">Text is available under the <a rel="license" href="//en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License">Creative Commons Attribution-ShareAlike License</a><a rel="license" href="//creativecommons.org/licenses/by-sa/3.0/" style="display:none;"></a>;
additional terms may apply.  By using this site, you agree to the <a href="//foundation.wikimedia.org/wiki/Terms_of_Use">Terms of Use</a> and <a href="//foundation.wikimedia.org/wiki/Privacy_policy">Privacy Policy</a>. Wikipedia® is a registered trademark of the <a href="//www.wikimediafoundation.org/">Wikimedia Foundation, Inc.</a>, a non-profit organization.</li>
	</ul>
	<ul id="footer-places" >
		<li id="footer-places-privacy"><a href="https://foundation.wikimedia.org/wiki/Privacy_policy" class="extiw" title="wmf:Privacy policy">Privacy policy</a></li>
		<li id="footer-places-about"><a href="/wiki/Wikipedia:About" title="Wikipedia:About">About Wikipedia</a></li>
		<li id="footer-places-disclaimer"><a href="/wiki/Wikipedia:General_disclaimer" title="Wikipedia:General disclaimer">Disclaimers</a></li>
		<li id="footer-places-contact"><a href="//en.wikipedia.org/wiki/Wikipedia:Contact_us">Contact Wikipedia</a></li>
		<li id="footer-places-developers"><a href="https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute">Developers</a></li>
		<li id="footer-places-statslink"><a href="https://stats.wikimedia.org/#/en.wikipedia.org">Statistics</a></li>
		<li id="footer-places-cookiestatement"><a href="https://foundation.wikimedia.org/wiki/Cookie_statement">Cookie statement</a></li>
		<li id="footer-places-mobileview"><a href="//en.m.wikipedia.org/w/index.php?title=Web_development&amp;mobileaction=toggle_view_mobile" class="noprint stopMobileRedirectToggle">Mobile view</a></li>
	</ul>
	<ul id="footer-icons" class="noprint">
		<li id="footer-copyrightico"><a href="https://wikimediafoundation.org/"><img src="/static/images/wikimedia-button.png" srcset="/static/images/wikimedia-button-1.5x.png 1.5x, /static/images/wikimedia-button-2x.png 2x" width="88" height="31" alt="Wikimedia Foundation"/></a></li>
		<li id="footer-poweredbyico"><a href="https://www.mediawiki.org/"><img src="/static/images/poweredby_mediawiki_88x31.png" alt="Powered by MediaWiki" srcset="/static/images/poweredby_mediawiki_132x47.png 1.5x, /static/images/poweredby_mediawiki_176x62.png 2x" width="88" height="31"/></a></li>
	</ul>
	<div style="clear: both;"></div>
</div>


<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgPageParseReport":{"limitreport":{"cputime":"0.276","walltime":"0.422","ppvisitednodes":{"value":540,"limit":1000000},"postexpandincludesize":{"value":20809,"limit":2097152},"templateargumentsize":{"value":396,"limit":2097152},"expansiondepth":{"value":13,"limit":40},"expensivefunctioncount":{"value":6,"limit":500},"unstrip-depth":{"value":1,"limit":20},"unstrip-size":{"value":11362,"limit":5000000},"entityaccesscount":{"value":1,"limit":400},"timingprofile":["100.00%  380.920      1 -total"," 29.73%  113.239      1 Template:Reflist"," 25.30%   96.374      1 Template:Refimprove"," 24.15%   91.977      2 Template:Cite_web"," 23.64%   90.041      2 Template:Ambox"," 18.91%   72.034      1 Template:Pp-semi"," 13.41%   51.085      1 Template:Authority_control"," 10.56%   40.215      1 Template:Find_sources_mainspace","  7.49%   28.536      1 Template:Essay-like","  5.10%   19.432      1 Template:DMCA"]},"scribunto":{"limitreport-timeusage":{"value":"0.172","limit":"10.000"},"limitreport-memusage":{"value":3788085,"limit":52428800}},"cachereport":{"origin":"mw1366","timestamp":"20200516045241","ttl":2592000,"transientcontent":false}}});});</script>
<script type="application/ld+json">{"@context":"https:\/\/schema.org","@type":"Article","name":"Web development","url":"https:\/\/en.wikipedia.org\/wiki\/Web_development","sameAs":"http:\/\/www.wikidata.org\/entity\/Q386275","mainEntity":"http:\/\/www.wikidata.org\/entity\/Q386275","author":{"@type":"Organization","name":"Contributors to Wikimedia projects"},"publisher":{"@type":"Organization","name":"Wikimedia Foundation, Inc.","logo":{"@type":"ImageObject","url":"https:\/\/www.wikimedia.org\/static\/images\/wmf-hor-googpub.png"}},"datePublished":"2004-04-22T10:01:27Z","dateModified":"2020-02-10T10:52:10Z","headline":"Job of building websites within the Internet or an intranet"}</script>
<script>(RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":95,"wgHostname":"mw1395"});});</script></body></html>

		""")
