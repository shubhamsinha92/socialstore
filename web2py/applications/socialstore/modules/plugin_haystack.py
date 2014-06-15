




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>web2py-haystack/modules/plugin_haystack.py at master · mdipierro/web2py-haystack · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="mdipierro/web2py-haystack" name="twitter:title" /><meta content="web2py-haystack - A full-text search engine for web2py named after Django-Haystack (since serves a similar purpose)" name="twitter:description" /><meta content="https://avatars3.githubusercontent.com/u/965839?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars3.githubusercontent.com/u/965839?s=400" property="og:image" /><meta content="mdipierro/web2py-haystack" property="og:title" /><meta content="https://github.com/mdipierro/web2py-haystack" property="og:url" /><meta content="web2py-haystack - A full-text search engine for web2py named after Django-Haystack (since serves a similar purpose)" property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="63793AE4:4C66:3B0E183:5395501B" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico" />


    <meta content="authenticity_token" name="csrf-param" />
<meta content="M0ue6/PbvSVz5Cd2flh+lOMyjNeNUZTcPs2l3PIHGJ1AVj0hv1LMFM7Q0elnyVbxAvO3VqM9zH+iUMyoWBLEzg==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-1aeb426322c64c12b92d56bda5b110fc1093f75e.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-b2cccfcac1a522b6ce675606f61388d36bf2c080.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="6b9e40027b6fe719e1c3d0a9180a2d6a">

      
  <meta name="description" content="web2py-haystack - A full-text search engine for web2py named after Django-Haystack (since serves a similar purpose)" />

  <meta content="965839" name="octolytics-dimension-user_id" /><meta content="mdipierro" name="octolytics-dimension-user_login" /><meta content="11704350" name="octolytics-dimension-repository_id" /><meta content="mdipierro/web2py-haystack" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="11704350" name="octolytics-dimension-repository_network_root_id" /><meta content="mdipierro/web2py-haystack" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/mdipierro/web2py-haystack/commits/master.atom" rel="alternate" title="Recent Commits to web2py-haystack:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production linux vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fmdipierro%2Fweb2py-haystack%2Fblob%2Fmaster%2Fmodules%2Fplugin_haystack.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="mdipierro/web2py-haystack"
      data-branch="master"
      data-sha="8885b4b14b9e17d208085e4d36eac0ef721e0454"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="mdipierro/web2py-haystack" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
    <a href="/login?return_to=%2Fmdipierro%2Fweb2py-haystack"
    class="minibutton with-count star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>Star
  </a>

    <a class="social-count js-social-count" href="/mdipierro/web2py-haystack/stargazers">
      9
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fmdipierro%2Fweb2py-haystack"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>Fork
      </a>
      <a href="/mdipierro/web2py-haystack/network" class="social-count">
        2
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/mdipierro" class="url fn" itemprop="url" rel="author"><span itemprop="title">mdipierro</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/mdipierro/web2py-haystack" class="js-current-repository js-repo-home-link">web2py-haystack</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/mdipierro/web2py-haystack" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /mdipierro/web2py-haystack">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/mdipierro/web2py-haystack/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues /mdipierro/web2py-haystack/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>1</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/mdipierro/web2py-haystack/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /mdipierro/web2py-haystack/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>1</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/mdipierro/web2py-haystack/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /mdipierro/web2py-haystack/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/mdipierro/web2py-haystack/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /mdipierro/web2py-haystack/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/mdipierro/web2py-haystack/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /mdipierro/web2py-haystack/network">
          <span class="octicon octicon-repo-forked"></span> <span class="full-word">Network</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/mdipierro/web2py-haystack.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/mdipierro/web2py-haystack.git" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/mdipierro/web2py-haystack" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/mdipierro/web2py-haystack" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>



                <a href="/mdipierro/web2py-haystack/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download mdipierro/web2py-haystack as a zip file"
                   title="Download mdipierro/web2py-haystack as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/mdipierro/web2py-haystack/blob/54a24176782363517018ef847a794bb4783823d2/modules/plugin_haystack.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:dd0c2d4a0f39009e74bc012be71fff03 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/mdipierro/web2py-haystack/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/mdipierro/web2py-haystack/blob/master/modules/plugin_haystack.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/mdipierro/web2py-haystack" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">web2py-haystack</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/mdipierro/web2py-haystack/tree/master/modules" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">modules</span></a></span><span class="separator"> / </span><strong class="final-path">plugin_haystack.py</strong> <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="modules/plugin_haystack.py" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>
</div>


  <div class="commit file-history-tease">
      <img alt="mdipierro" class="main-avatar js-avatar" data-user="965839" height="24" src="https://avatars0.githubusercontent.com/u/965839?s=140" width="24" />
      <span class="author"><a href="/mdipierro" rel="author">mdipierro</a></span>
      <time datetime="2013-12-16T21:23:37-06:00" is="relative-time">December 16, 2013</time>
      <div class="commit-title">
          <a href="/mdipierro/web2py-haystack/commit/54a24176782363517018ef847a794bb4783823d2" class="message" data-pjax="true" title="varous improvements, thanks Alex Bush">varous improvements, thanks Alex Bush</a>
      </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong>  contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="mdipierro" class=" js-avatar" data-user="965839" height="24" src="https://avatars0.githubusercontent.com/u/965839?s=140" width="24" />
            <a href="/mdipierro">mdipierro</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
        <span class="meta-divider"></span>
          <span>273 lines (259 sloc)</span>
          <span class="meta-divider"></span>
        <span>11.454 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped tooltipped-w" href="#"
                 aria-label="You must be signed in to make or propose changes">Edit</a>
          <a href="/mdipierro/web2py-haystack/raw/master/modules/plugin_haystack.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/mdipierro/web2py-haystack/blame/master/modules/plugin_haystack.py" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/mdipierro/web2py-haystack/commits/master/modules/plugin_haystack.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-python js-blob-data">
       <table class="file-code file-diff tab-size-8">
         <tr class="file-code-line">
           <td class="blob-line-nums">
             <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC2'><span class="sd">plugin_haystack.py</span></div><div class='line' id='LC3'><br/></div><div class='line' id='LC4'><span class="sd">This file is an experimental part of the web2py.</span></div><div class='line' id='LC5'><span class="sd">It allows full text search using database, Whoosh, or Solr.</span></div><div class='line' id='LC6'><span class="sd">Author: Massimo Di Pierro</span></div><div class='line' id='LC7'><span class="sd">License: LGPL</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="sd">Usage:</span></div><div class='line' id='LC10'><span class="sd">db = DAL()</span></div><div class='line' id='LC11'><span class="sd">db.define_table(&#39;thing&#39;,Field(&#39;name&#39;),Field(&#39;description&#39;))</span></div><div class='line' id='LC12'><span class="sd">index = Haystack(db.thing)                        # table to be indexed</span></div><div class='line' id='LC13'><span class="sd">index.indexes(&#39;name&#39;,&#39;description&#39;)               # fields to be indexed</span></div><div class='line' id='LC14'><span class="sd">db.thing.insert(name=&#39;Char&#39;,description=&#39;A char&#39;) # automatically indexed</span></div><div class='line' id='LC15'><span class="sd">db(db.thing.id).update(description=&#39;The chair&#39;)   # automatically re-indexed</span></div><div class='line' id='LC16'><span class="sd">db(db.thing).delete()                             # automatically re-indexed</span></div><div class='line' id='LC17'><span class="sd">query = index.search(name=&#39;chair&#39;,description=&#39;the&#39;)</span></div><div class='line' id='LC18'><span class="sd">print db(query).select()</span></div><div class='line' id='LC19'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'><span class="kn">import</span> <span class="nn">re</span></div><div class='line' id='LC22'><span class="kn">import</span> <span class="nn">os</span></div><div class='line' id='LC23'><span class="kn">from</span> <span class="nn">gluon</span> <span class="kn">import</span> <span class="n">Field</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'><span class="n">DEBUG</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><span class="k">class</span> <span class="nc">SimpleBackend</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">regex</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s">&#39;[\w\-]{2}[\w\-]+&#39;</span><span class="p">)</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ignore</span> <span class="o">=</span> <span class="nb">set</span><span class="p">([</span><span class="s">&#39;and&#39;</span><span class="p">,</span><span class="s">&#39;or&#39;</span><span class="p">,</span><span class="s">&#39;in&#39;</span><span class="p">,</span><span class="s">&#39;of&#39;</span><span class="p">,</span><span class="s">&#39;for&#39;</span><span class="p">,</span><span class="s">&#39;to&#39;</span><span class="p">,</span><span class="s">&#39;from&#39;</span><span class="p">])</span></div><div class='line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">table</span><span class="p">,</span> <span class="n">db</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">table</span> <span class="o">=</span> <span class="n">table</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">db</span> <span class="o">=</span> <span class="n">db</span> <span class="ow">or</span> <span class="n">table</span><span class="o">.</span><span class="n">_db</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">idx</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="o">.</span><span class="n">define_table</span><span class="p">(</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;haystack_</span><span class="si">%s</span><span class="s">&#39;</span> <span class="o">%</span> <span class="n">table</span><span class="o">.</span><span class="n">_tablename</span><span class="p">,</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Field</span><span class="p">(</span><span class="s">&#39;fieldname&#39;</span><span class="p">),</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Field</span><span class="p">(</span><span class="s">&#39;keyword&#39;</span><span class="p">),</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Field</span><span class="p">(</span><span class="s">&#39;record_id&#39;</span><span class="p">,</span><span class="s">&#39;integer&#39;</span><span class="p">))</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">indexes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">fieldnames</span><span class="p">):</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fieldnames</span> <span class="o">=</span> <span class="n">fieldnames</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">after_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">fields</span><span class="p">,</span><span class="nb">id</span><span class="p">):</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="s">&#39;after insert&#39;</span><span class="p">,</span><span class="n">fields</span><span class="p">,</span><span class="nb">id</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">fieldname</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fieldnames</span><span class="p">:</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">words</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">regex</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">fields</span><span class="p">[</span><span class="n">fieldname</span><span class="p">]</span><span class="o">.</span><span class="n">lower</span><span class="p">()))</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">ignore</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">words</span><span class="p">:</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fieldname</span> <span class="o">=</span> <span class="n">fieldname</span><span class="p">,</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">keyword</span> <span class="o">=</span> <span class="n">word</span><span class="p">,</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">record_id</span> <span class="o">=</span> <span class="nb">id</span><span class="p">)</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="p">)</span><span class="o">.</span><span class="n">select</span><span class="p">()</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">after_update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">queryset</span><span class="p">,</span><span class="n">fields</span><span class="p">):</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="s">&#39;after update&#39;</span><span class="p">,</span><span class="n">queryset</span><span class="p">,</span><span class="n">fields</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_ids</span><span class="p">(</span><span class="n">queryset</span><span class="p">):</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">fieldname</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fieldnames</span><span class="p">:</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">fieldname</span> <span class="ow">in</span> <span class="n">fields</span><span class="p">:</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">words</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">regex</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">fields</span><span class="p">[</span><span class="n">fieldname</span><span class="p">]</span><span class="o">.</span><span class="n">lower</span><span class="p">()))</span> <span class="o">-</span> <span class="bp">self</span><span class="o">.</span><span class="n">ignore</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">existing_words</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">r</span><span class="o">.</span><span class="n">keyword</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">db</span><span class="p">(</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">fieldname</span> <span class="o">==</span> <span class="n">fieldname</span><span class="p">)</span><span class="o">&amp;</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">record_id</span><span class="o">==</span><span class="nb">id</span><span class="p">)</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">keyword</span><span class="p">))</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span><span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">fieldname</span> <span class="o">==</span> <span class="n">fieldname</span><span class="p">)</span><span class="o">&amp;</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">record_id</span><span class="o">==</span><span class="nb">id</span><span class="p">)</span><span class="o">&amp;</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">keyword</span><span class="o">.</span><span class="n">belongs</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">existing_words</span> <span class="o">-</span> <span class="n">words</span><span class="p">)))</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">new_word</span> <span class="ow">in</span> <span class="p">(</span><span class="n">words</span> <span class="o">-</span> <span class="n">existing_words</span><span class="p">):</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fieldname</span> <span class="o">=</span> <span class="n">fieldname</span><span class="p">,</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">keyword</span> <span class="o">=</span> <span class="n">new_word</span><span class="p">,</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">record_id</span> <span class="o">=</span> <span class="nb">id</span><span class="p">)</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="p">)</span><span class="o">.</span><span class="n">select</span><span class="p">()</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_ids</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">queryset</span><span class="p">):</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="n">r</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">queryset</span><span class="o">.</span><span class="n">select</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="o">.</span><span class="n">_id</span><span class="p">)]</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">after_delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">queryset</span><span class="p">):</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="s">&#39;after delete&#39;</span><span class="p">,</span><span class="n">queryset</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_ids</span><span class="p">(</span><span class="n">queryset</span><span class="p">)</span></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">record_id</span><span class="o">.</span><span class="n">belongs</span><span class="p">(</span><span class="n">ids</span><span class="p">))</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="p">)</span><span class="o">.</span><span class="n">select</span><span class="p">()</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC82'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">meta_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">limit</span><span class="p">,</span><span class="n">mode</span><span class="p">,</span><span class="o">**</span><span class="n">fieldkeys</span><span class="p">):</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">db</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">fieldname</span> <span class="ow">in</span> <span class="n">fieldkeys</span><span class="p">:</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">fieldname</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fieldnames</span><span class="p">:</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">words</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">regex</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span><span class="n">fieldkeys</span><span class="p">[</span><span class="n">fieldname</span><span class="p">]</span><span class="o">.</span><span class="n">lower</span><span class="p">()))</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">meta_query</span> <span class="o">=</span> <span class="p">((</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">fieldname</span><span class="o">==</span><span class="n">fieldname</span><span class="p">)</span><span class="o">&amp;</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">idx</span><span class="o">.</span><span class="n">keyword</span><span class="o">.</span><span class="n">belongs</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">words</span><span class="p">))))</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">new_ids</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">r</span><span class="o">.</span><span class="n">record_id</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">db</span><span class="p">(</span><span class="n">meta_query</span><span class="p">)</span><span class="o">.</span><span class="n">select</span><span class="p">(</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">limitby</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">limit</span><span class="p">)))</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">mode</span> <span class="o">==</span> <span class="s">&#39;and&#39;</span><span class="p">:</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="n">new_ids</span> <span class="k">if</span> <span class="n">ids</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">ids</span> <span class="o">&amp;</span> <span class="n">new_ids</span></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">mode</span> <span class="o">==</span> <span class="s">&#39;or&#39;</span><span class="p">:</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="n">new_ids</span> <span class="k">if</span> <span class="n">ids</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">ids</span> <span class="o">|</span> <span class="n">new_ids</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span></div><div class='line' id='LC97'><br/></div><div class='line' id='LC98'><br/></div><div class='line' id='LC99'><span class="k">class</span> <span class="nc">WhooshBackend</span><span class="p">(</span><span class="n">SimpleBackend</span><span class="p">):</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">table</span><span class="p">,</span> <span class="n">indexdir</span><span class="p">):</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">table</span> <span class="o">=</span> <span class="n">table</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">indexdir</span> <span class="o">=</span> <span class="n">indexdir</span></div><div class='line' id='LC103'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">indexdir</span><span class="p">):</span></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="n">indexdir</span><span class="p">)</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">indexes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">fieldnames</span><span class="p">):</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">whoosh.index</span> <span class="kn">import</span> <span class="n">create_in</span></div><div class='line' id='LC108'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">whoosh.fields</span> <span class="kn">import</span> <span class="n">Schema</span><span class="p">,</span> <span class="n">TEXT</span><span class="p">,</span> <span class="n">ID</span></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s">&quot;Cannot find Whoosh&quot;</span><span class="p">)</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fieldnames</span> <span class="o">=</span> <span class="n">fieldnames</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">ix</span> <span class="o">=</span> <span class="n">open_dir</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">indexdir</span><span class="p">)</span></div><div class='line' id='LC114'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">schema</span> <span class="o">=</span> <span class="n">Schema</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="n">ID</span><span class="p">(</span><span class="n">unique</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span><span class="n">stored</span><span class="o">=</span><span class="bp">True</span><span class="p">),</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">**</span><span class="nb">dict</span><span class="p">((</span><span class="n">k</span><span class="p">,</span><span class="n">TEXT</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">fieldnames</span><span class="p">))</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">ix</span> <span class="o">=</span> <span class="n">create_in</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">indexdir</span><span class="p">,</span> <span class="n">schema</span><span class="p">)</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">after_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">fields</span><span class="p">,</span><span class="nb">id</span><span class="p">):</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="s">&#39;after insert&#39;</span><span class="p">,</span><span class="n">fields</span><span class="p">,</span><span class="nb">id</span></div><div class='line' id='LC120'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ix</span><span class="o">.</span><span class="n">writer</span><span class="p">()</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span><span class="o">.</span><span class="n">add_document</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="nb">unicode</span><span class="p">(</span><span class="nb">id</span><span class="p">),</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">**</span><span class="nb">dict</span><span class="p">((</span><span class="n">name</span><span class="p">,</span><span class="nb">unicode</span><span class="p">(</span><span class="n">fields</span><span class="p">[</span><span class="n">name</span><span class="p">]))</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fieldnames</span> <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">fields</span><span class="p">))</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">after_update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">queryset</span><span class="p">,</span><span class="n">fields</span><span class="p">):</span></div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="s">&#39;after update&#39;</span><span class="p">,</span><span class="n">queryset</span><span class="p">,</span><span class="n">fields</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_ids</span><span class="p">(</span><span class="n">queryset</span><span class="p">)</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">ids</span><span class="p">:</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ix</span><span class="o">.</span><span class="n">writer</span><span class="p">()</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">ids</span><span class="p">:</span></div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span><span class="o">.</span><span class="n">update_document</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="nb">unicode</span><span class="p">(</span><span class="nb">id</span><span class="p">),</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">**</span><span class="nb">dict</span><span class="p">((</span><span class="n">name</span><span class="p">,</span><span class="nb">unicode</span><span class="p">(</span><span class="n">fields</span><span class="p">[</span><span class="n">name</span><span class="p">]))</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fieldnames</span> <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">fields</span><span class="p">))</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">after_delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">queryset</span><span class="p">):</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="s">&#39;after delete&#39;</span><span class="p">,</span><span class="n">queryset</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_ids</span><span class="p">(</span><span class="n">queryset</span><span class="p">)</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">ids</span><span class="p">:</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">ix</span><span class="o">.</span><span class="n">writer</span><span class="p">()</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">ids</span><span class="p">:</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span><span class="o">.</span><span class="n">delete_by_term</span><span class="p">(</span><span class="s">&#39;id&#39;</span><span class="p">,</span> <span class="nb">unicode</span><span class="p">(</span><span class="nb">id</span><span class="p">))</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">writer</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">meta_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">limit</span><span class="p">,</span><span class="n">mode</span><span class="p">,</span><span class="o">**</span><span class="n">fieldkeys</span><span class="p">):</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">whoosh.qparser</span> <span class="kn">import</span> <span class="n">QueryParser</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">ix</span><span class="o">.</span><span class="n">searcher</span><span class="p">()</span> <span class="k">as</span> <span class="n">searcher</span><span class="p">:</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">fieldname</span> <span class="ow">in</span> <span class="n">fieldkeys</span><span class="p">:</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">parser</span> <span class="o">=</span> <span class="n">QueryParser</span><span class="p">(</span><span class="n">fieldname</span><span class="p">,</span> <span class="n">schema</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">ix</span><span class="o">.</span><span class="n">schema</span><span class="p">)</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">query</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse</span><span class="p">(</span><span class="nb">unicode</span><span class="p">(</span><span class="n">fieldkeys</span><span class="p">[</span><span class="n">fieldname</span><span class="p">]))</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">results</span> <span class="o">=</span> <span class="n">searcher</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">query</span><span class="p">,</span><span class="n">limit</span><span class="o">=</span><span class="n">limit</span><span class="p">)</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">new_ids</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="nb">long</span><span class="p">(</span><span class="n">result</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">])</span> <span class="k">for</span> <span class="n">result</span> <span class="ow">in</span> <span class="n">results</span><span class="p">)</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">mode</span> <span class="o">==</span> <span class="s">&#39;and&#39;</span><span class="p">:</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="n">new_ids</span> <span class="k">if</span> <span class="n">ids</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">ids</span> <span class="o">&amp;</span> <span class="n">new_ids</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">mode</span> <span class="o">==</span> <span class="s">&#39;or&#39;</span><span class="p">:</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="n">new_ids</span> <span class="k">if</span> <span class="n">ids</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">ids</span> <span class="o">|</span> <span class="n">new_ids</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span></div><div class='line' id='LC160'><br/></div><div class='line' id='LC161'><br/></div><div class='line' id='LC162'><span class="k">class</span> <span class="nc">SolrBackend</span><span class="p">(</span><span class="n">SimpleBackend</span><span class="p">):</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">table</span><span class="p">,</span> <span class="n">url</span><span class="o">=</span><span class="s">&quot;http://localhost:8983&quot;</span><span class="p">,</span><span class="n">schema_filename</span><span class="o">=</span><span class="s">&quot;schema.xml&quot;</span><span class="p">):</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">table</span> <span class="o">=</span> <span class="n">table</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">url</span> <span class="o">=</span> <span class="n">url</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">schema_filename</span><span class="o">=</span><span class="n">schema_filename</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">indexes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">fieldnames</span><span class="p">):</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">import</span> <span class="nn">sunburnt</span></div><div class='line' id='LC170'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">ImportError</span><span class="p">(</span><span class="s">&quot;Cannot find sunburnt, it is necessary to access Solr&quot;</span><span class="p">)</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">fieldnames</span> <span class="o">=</span> <span class="n">fieldnames</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema_filename</span><span class="p">):</span></div><div class='line' id='LC174'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">schema</span><span class="o">=</span><span class="s">&#39;&lt;fields&gt;&lt;field name=&quot;id&quot; type=&quot;int&quot; indexed=&quot;true&quot; stored=&quot;true&quot; required=&quot;true&quot; /&gt;</span><span class="si">%s</span><span class="s">&lt;/fields&gt;&#39;</span> \</div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="o">%</span> <span class="s">&#39;&#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s">&#39;&lt;field name=&quot;</span><span class="si">%s</span><span class="s">&quot; type=&quot;string&quot; /&gt;&#39;</span> <span class="o">%</span> <span class="n">name</span> <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">fieldname</span><span class="p">)</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">schema_filename</span><span class="p">,</span><span class="s">&#39;w&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">shema</span><span class="p">)</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">interface</span> <span class="o">=</span> <span class="n">sunburnt</span><span class="o">.</span><span class="n">SolrInterface</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">schema_filename</span><span class="p">)</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s">&quot;Cannot connect to Solr: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="bp">self</span><span class="o">.</span><span class="n">url</span><span class="p">)</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">after_insert</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">fields</span><span class="p">,</span><span class="nb">id</span><span class="p">):</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="s">&#39;after insert&#39;</span><span class="p">,</span><span class="n">fields</span><span class="p">,</span><span class="nb">id</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">document</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;id&#39;</span><span class="p">:</span><span class="nb">id</span><span class="p">}</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fieldnames</span><span class="p">:</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">fields</span><span class="p">:</span></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">document</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">unicode</span><span class="p">(</span><span class="n">fields</span><span class="p">[</span><span class="n">name</span><span class="p">])</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="o">.</span><span class="n">add</span><span class="p">([</span><span class="n">document</span><span class="p">])</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">after_update</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">queryset</span><span class="p">,</span><span class="n">fields</span><span class="p">):</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; caveat, this should work but only if ALL indexed fields are updated at once &quot;&quot;&quot;</span></div><div class='line' id='LC192'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="s">&#39;after update&#39;</span><span class="p">,</span><span class="n">queryset</span><span class="p">,</span><span class="n">fields</span></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_ids</span><span class="p">(</span><span class="n">queryset</span><span class="p">)</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">documents</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">ids</span><span class="p">:</span></div><div class='line' id='LC197'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">document</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;id&#39;</span><span class="p">:</span><span class="nb">id</span><span class="p">}</span></div><div class='line' id='LC198'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">fieldnames</span><span class="p">:</span></div><div class='line' id='LC199'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">fields</span><span class="p">:</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">document</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="nb">unicode</span><span class="p">(</span><span class="n">fields</span><span class="p">[</span><span class="n">name</span><span class="p">])</span></div><div class='line' id='LC201'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">documents</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">document</span><span class="p">)</span></div><div class='line' id='LC202'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">documents</span><span class="p">)</span></div><div class='line' id='LC203'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC205'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">after_delete</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">queryset</span><span class="p">):</span></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">DEBUG</span><span class="p">:</span> <span class="k">print</span> <span class="s">&#39;after delete&#39;</span><span class="p">,</span><span class="n">queryset</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_ids</span><span class="p">(</span><span class="n">queryset</span><span class="p">)</span></div><div class='line' id='LC208'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="o">.</span><span class="n">delete</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span></div><div class='line' id='LC209'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span></div><div class='line' id='LC210'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">meta_search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">limit</span><span class="p">,</span><span class="n">mode</span><span class="p">,</span><span class="o">**</span><span class="n">fieldkeys</span><span class="p">):</span></div><div class='line' id='LC212'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot; mode is ignored hhere since I am not sure what Solr does  &quot;&quot;&quot;</span></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">results</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">interface</span><span class="o">.</span><span class="n">query</span><span class="p">(</span><span class="o">**</span><span class="n">fieldkeys</span><span class="p">)</span><span class="o">.</span><span class="n">paginate</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">limit</span><span class="p">)</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="p">[</span><span class="n">r</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">]</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">results</span><span class="p">]</span></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ids</span></div><div class='line' id='LC216'><br/></div><div class='line' id='LC217'><br/></div><div class='line' id='LC218'><span class="k">class</span> <span class="nc">Haystack</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">table</span><span class="p">,</span><span class="n">backend</span><span class="o">=</span><span class="n">SimpleBackend</span><span class="p">,</span><span class="o">**</span><span class="n">attr</span><span class="p">):</span></div><div class='line' id='LC220'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">table</span> <span class="o">=</span> <span class="n">table</span></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">backend</span> <span class="o">=</span> <span class="n">backend</span><span class="p">(</span><span class="n">table</span><span class="p">,</span><span class="o">**</span><span class="n">attr</span><span class="p">)</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">indexes</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="o">*</span><span class="n">fieldnames</span><span class="p">):</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">invalid</span> <span class="o">=</span> <span class="p">[</span><span class="n">f</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">fieldnames</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">f</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="o">.</span><span class="n">fields</span><span class="p">()</span> <span class="ow">or</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="p">[</span><span class="n">f</span><span class="p">]</span><span class="o">.</span><span class="n">type</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&#39;string&#39;</span><span class="p">,</span><span class="s">&#39;text&#39;</span><span class="p">)]</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">invalid</span><span class="p">:</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s">&quot;Unable to index fields: </span><span class="si">%s</span><span class="s">&quot;</span> <span class="o">%</span> <span class="s">&#39;, &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">invalid</span><span class="p">))</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">backend</span><span class="o">.</span><span class="n">indexes</span><span class="p">(</span><span class="o">*</span><span class="n">fieldnames</span><span class="p">)</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="o">.</span><span class="n">_after_insert</span><span class="o">.</span><span class="n">append</span><span class="p">(</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">lambda</span> <span class="n">fields</span><span class="p">,</span><span class="nb">id</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">backend</span><span class="o">.</span><span class="n">after_insert</span><span class="p">(</span><span class="n">fields</span><span class="p">,</span><span class="nb">id</span><span class="p">))</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="o">.</span><span class="n">_after_update</span><span class="o">.</span><span class="n">append</span><span class="p">(</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">lambda</span> <span class="n">queryset</span><span class="p">,</span><span class="n">fields</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">backend</span><span class="o">.</span><span class="n">after_update</span><span class="p">(</span><span class="n">queryset</span><span class="p">,</span><span class="n">fields</span><span class="p">))</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="o">.</span><span class="n">_after_delete</span><span class="o">.</span><span class="n">append</span><span class="p">(</span></div><div class='line' id='LC233'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">lambda</span> <span class="n">queryset</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">backend</span><span class="o">.</span><span class="n">after_delete</span><span class="p">(</span><span class="n">queryset</span><span class="p">))</span></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">search</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span><span class="n">limit</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span><span class="n">mode</span><span class="o">=</span><span class="s">&#39;and&#39;</span><span class="p">,</span><span class="o">**</span><span class="n">fieldkeys</span><span class="p">):</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ids</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">backend</span><span class="o">.</span><span class="n">meta_search</span><span class="p">(</span><span class="n">limit</span><span class="p">,</span><span class="n">mode</span><span class="p">,</span><span class="o">**</span><span class="n">fieldkeys</span><span class="p">)</span></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">table</span><span class="o">.</span><span class="n">_id</span><span class="o">.</span><span class="n">belongs</span><span class="p">(</span><span class="n">ids</span><span class="p">)</span></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'><span class="k">def</span> <span class="nf">test</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s">&#39;simple&#39;</span><span class="p">):</span></div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span> <span class="o">=</span> <span class="n">DAL</span><span class="p">()</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span><span class="o">.</span><span class="n">define_table</span><span class="p">(</span><span class="s">&#39;thing&#39;</span><span class="p">,</span><span class="n">Field</span><span class="p">(</span><span class="s">&#39;name&#39;</span><span class="p">),</span><span class="n">Field</span><span class="p">(</span><span class="s">&#39;description&#39;</span><span class="p">,</span><span class="s">&#39;text&#39;</span><span class="p">))</span></div><div class='line' id='LC241'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">mode</span><span class="o">==</span><span class="s">&#39;simple&#39;</span><span class="p">:</span></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">index</span> <span class="o">=</span> <span class="n">Haystack</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">thing</span><span class="p">)</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">mode</span><span class="o">==</span><span class="s">&#39;whoosh&#39;</span><span class="p">:</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">index</span> <span class="o">=</span> <span class="n">Haystack</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">thing</span><span class="p">,</span><span class="n">backend</span><span class="o">=</span><span class="n">WhooshBackend</span><span class="p">,</span><span class="n">indexdir</span><span class="o">=</span><span class="s">&#39;test-whoosh&#39;</span><span class="p">)</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="n">mode</span><span class="o">==</span><span class="s">&#39;solr&#39;</span><span class="p">:</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">index</span> <span class="o">=</span> <span class="n">Haystack</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">thing</span><span class="p">,</span><span class="n">backend</span><span class="o">=</span><span class="n">SolrBackend</span><span class="p">,</span><span class="n">url</span><span class="o">=</span><span class="s">&#39;https://localhost:8983&#39;</span><span class="p">)</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">index</span><span class="o">.</span><span class="n">indexes</span><span class="p">(</span><span class="s">&#39;name&#39;</span><span class="p">,</span><span class="s">&#39;description&#39;</span><span class="p">)</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">id</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">thing</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&quot;table&quot;</span><span class="p">,</span><span class="n">description</span> <span class="o">=</span> <span class="s">&quot;one table&quot;</span><span class="p">)</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">id</span> <span class="o">=</span> <span class="n">db</span><span class="o">.</span><span class="n">thing</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&quot;table&quot;</span><span class="p">,</span><span class="n">description</span> <span class="o">=</span> <span class="s">&quot;another table&quot;</span><span class="p">)</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;one&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">1</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">2</span></div><div class='line' id='LC252'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">2</span></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">,</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">2</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">thing</span><span class="o">.</span><span class="n">id</span><span class="o">==</span><span class="nb">id</span><span class="p">)</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">,</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;four legs&#39;</span><span class="p">)</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;another&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">0</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;four&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">1</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;legs&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">1</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;legs four&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">1</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">2</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">,</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">1</span></div><div class='line' id='LC261'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">)</span><span class="o">|</span></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">2</span></div><div class='line' id='LC263'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">thing</span><span class="o">.</span><span class="n">id</span><span class="o">==</span><span class="nb">id</span><span class="p">)</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">1</span></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span><span class="p">(</span><span class="n">db</span><span class="o">.</span><span class="n">thing</span><span class="p">)</span><span class="o">.</span><span class="n">delete</span><span class="p">()</span></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">assert</span> <span class="n">db</span><span class="p">(</span><span class="n">index</span><span class="o">.</span><span class="n">search</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s">&#39;table&#39;</span><span class="p">))</span><span class="o">.</span><span class="n">count</span><span class="p">()</span><span class="o">==</span><span class="mi">0</span></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span></div><div class='line' id='LC268'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">db</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div><div class='line' id='LC269'><br/></div><div class='line' id='LC270'><span class="k">if</span> <span class="n">__name__</span><span class="o">==</span><span class="s">&#39;__main__&#39;</span><span class="p">:</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">test</span><span class="p">(</span><span class="s">&#39;simple&#39;</span><span class="p">)</span></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">test</span><span class="p">(</span><span class="s">&#39;whoosh&#39;</span><span class="p">)</span></div></pre></div></td>
         </tr>
       </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.02935s from github-fe134-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-e87aa86ffae369acf33a96bb6567b2b57183be57.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-100ee281915e20c71d6b0ff254fbbb70b3fcaf3a.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>

