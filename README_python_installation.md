# Python installation guide for Windows and Mac OS
Below guide was extract from https://realpython.com/installing-python/

<p class="h3 mb-2 text-muted">Table of Contents</p>
<ul>
<li><a href="#windows">Windows</a><ul>
<li><a href="#step-1-download-the-python-3-installer">Step 1: Download the Python 3 Installer</a></li>
<li><a href="#step-2-run-the-installer">Step 2: Run the Installer</a></li>
</ul>
</ul>
<ul>
<li><a href="#macos-mac-os-x">macOS / Mac OS X</a><ul>
<li><a href="#step-1-install-homebrew-part-1">Step 1: Install Homebrew (Part 1)</a></li>
<li><a href="#step-2-install-homebrew-part-2">Step 2: Install Homebrew (Part 2)</a></li>
<li><a href="#step-3-install-python">Step 3: Install Python</a></li>
</ul>
</ul>

<h2 id="windows">Windows</h2>
<p>It is highly unlikely that your Windows system shipped with Python already installed. Windows systems typically do not. Fortunately, installing does not involve much more than downloading the Python installer from the <a href="https://www.python.org">python.org website</a> and running it. Let&rsquo;s take a look at how to install Python 3 on Windows:</p>
<h3 id="step-1-download-the-python-3-installer">Step 1: Download the Python 3 Installer</h3>
<ol>
<li>Open a browser window and navigate to the <a href="https://www.python.org/downloads/windows/">Download page for Windows</a> at <a href="https://www.python.org/">python.org</a>.</li>
<li>Underneath the heading at the top that says <strong>Python Releases for Windows</strong>, click on the link for the <strong>Latest Python 3 Release - Python 3.x.x</strong>. (As of this writing, the latest is Python 3.6.5.)</li>
<li>Scroll to the bottom and select either <strong>Windows x86-64 executable installer</strong> for 64-bit or <strong>Windows x86 executable installer</strong> for 32-bit. (See below.)</li>
</ol>
<blockquote>
<h4 id="sidebar-32-bit-or-64-bit-python">Sidebar: 32-bit or 64-bit Python?</h4>
<p>For Windows, you can choose either the 32-bit or 64-bit installer. Here&rsquo;s what the difference between the two comes down to:</p>
<ul>
<li>If your system has a 32-bit processor, then you should choose the 32-bit installer.</li>
<li>On a 64-bit system, either installer will actually work for most purposes. The 32-bit version will generally use less memory, but the 64-bit version performs better for applications with intensive computation.</li>
<li>If you&rsquo;re unsure which version to pick, go with the 64-bit version.</li>
</ul>
<p><strong>Note:</strong> Remember that if you get this choice &ldquo;wrong&rdquo; and would like to switch to another version of Python, you can just uninstall Python and then re-install it by downloading another installer from <a href="https://python.org">python.org</a>.</p>
</blockquote>
<h3 id="step-2-run-the-installer">Step 2: Run the Installer</h3>
<p>Once you have chosen and downloaded an installer, simply run it by double-clicking on the downloaded file. A dialog should appear that looks something like this:</p>
<p><a href="https://github.com/skyap/alphabot2/blob/master/images/win-install-dialog.png" target="_blank"><img class="img-fluid mx-auto d-block w-66" src="https://github.com/skyap/alphabot2/blob/master/images/win-install-dialog.png" width="549" height="338" /></a></p>
<div class="alert alert-primary" role="alert">
<p><strong>Important:</strong> You want to be sure to check the box that says <strong>Add Python 3.x to PATH</strong> as shown to ensure that the interpreter will be placed in your execution path.</p>
</div>
<p>Then just click <strong>Install Now</strong>. That should be all there is to it. A few minutes later you should have a working Python 3 installation on your system.</p>

<h2 id="macos-mac-os-x">macOS / Mac OS X</h2>
<p>While current versions of macOS (previously known as &ldquo;Mac OS X&rdquo;) include a version of Python 2, it is likely out of date by a few months. Also, this tutorial series uses Python 3, so let&rsquo;s get you upgraded to that.</p>
<p>The best way we found to install Python 3 on macOS is through the <a href="https://brew.sh">Homebrew package manager</a>. This approach is also recommended by community guides like <a href="http://docs.python-guide.org/en/latest/starting/install3/osx/">The Hitchhiker&rsquo;s Guide to Python</a>.</p>
<h3 id="step-1-install-homebrew-part-1">Step 1: Install Homebrew (Part 1)</h3>
<p>To get started, you first want to install Homebrew:</p>
<ol>
<li>Open a browser and navigate to <a href="http://brew.sh/">http://brew.sh/</a>. After the page has finished loading, <strong>select the Homebrew bootstrap code under &ldquo;Install Homebrew&rdquo;</strong>. Then hit <span class="keys"><kbd class="key-command">Cmd</kbd><span>+</span><kbd class="key-c">C</kbd></span> to copy it to the clipboard. Make sure you&rsquo;ve captured the text of the complete command because otherwise the installation will fail.</li>
<li>Now you need to <strong>open a Terminal.app window, paste the Homebrew bootstrap code, and then hit</strong> <span class="keys"><kbd class="key-enter">Enter</kbd></span>. This will begin the Homebrew installation.</li>
<li>If you&rsquo;re doing this on a fresh install of macOS, you may get a pop up alert <strong>asking you to install Apple&rsquo;s &ldquo;command line developer tools&rdquo;</strong>. You&rsquo;ll need those to continue with the installation, so please <strong>confirm the dialog box by clicking on &ldquo;Install&rdquo;</strong>.</li>
</ol>
<p>At this point, you&rsquo;re likely waiting for the command line developer tools to finish installing, and that&rsquo;s going to take a few minutes. Time to grab a coffee or tea!</p>
<h3 id="step-2-install-homebrew-part-2">Step 2: Install Homebrew (Part 2)</h3>
<p>You can continue installing Homebrew and then Python after the command line developer tools installation is complete:</p>
<ol>
<li>Confirm the &ldquo;The software was installed&rdquo; dialog from the developer tools installer.</li>
<li>Back in the terminal, hit <span class="keys"><kbd class="key-enter">Enter</kbd></span> to continue with the Homebrew installation.</li>
<li>Homebrew asks you to enter your password so it can finalize the installation. <strong>Enter your user account password and hit</strong> <span class="keys"><kbd class="key-enter">Enter</kbd></span> to continue.</li>
<li>Depending on your internet connection, Homebrew will take a few minutes to download its required files. Once the installation is complete, you&rsquo;ll end up back at the command prompt in your terminal window.</li>
</ol>
<p>Whew! Now that the Homebrew package manager is set up, let&rsquo;s continue on with installing Python 3 on your system.</p>
<h3 id="step-3-install-python">Step 3: Install Python</h3>
<p>Once Homebrew has finished installing, <strong>return to your terminal and run the following command</strong>:</p>
<div class="highlight sh"><pre><span></span><span class="gp">$</span> brew install python3
</pre></div>
<div class="alert alert-primary" role="alert">
<p><strong>Note:</strong> When you copy this command, be sure you don&rsquo;t include the <code>$</code> character at the beginning. That&rsquo;s just an indicator that this is a console command.</p>
</div>
<p>This will download and install the latest version of Python. After the Homebrew <code>brew install</code> command finishes, Python 3 should be installed on your system.</p>
<p>You can make sure everything went correctly by testing if Python can be accessed from the terminal:</p>
<ol>
<li>Open the terminal by launching <strong>Terminal.app</strong>.</li>
<li>Type <code>pip3</code> and hit <span class="keys"><kbd class="key-enter">Enter</kbd></span>.</li>
<li>You should see the help text from Python&rsquo;s &ldquo;Pip&rdquo; package manager. If you get an error message running <code>pip3</code>, go through the Python install steps again to make sure you have a working Python installation.</li>
</ol>
<p>Assuming everything went well and you saw the output from Pip in your command prompt window&hellip;congratulations! You just installed Python on your system, and you&rsquo;re all set to continue with the next section in this tutorial.</p>



