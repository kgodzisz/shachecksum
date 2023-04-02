# shachecksum
<p>Script calculates the SHA256 checksum of the specified file and compares it with the value passed by us. This way we can make sure that the file we downloaded or simply have on the disk was not modified in any way. I'm creating a Docker image that I use. However, if you want, I can also provide just the script. Therefore, you can run it using Python installed on your local system.</p>

<p><strong>To download files from Github:</strong></p>
<code>git clone https://github.com/kgodzisz/shachecksum.git</code><br /><br />

<p><strong>Create your own image in your local repository:</strong></p>
<code>docker build -t shachecksum .</code><br /><br />

<p><strong>Run the tool:</strong></p>
<code>docker run --rm -v /path/to/file:/app shachecksum file-name file-checksum</code><br /><br />

<p>T<strong>he second way is to download the prepared file from the Docker Hub repository:</strong></p>
<code>docker run --rm -v /path/to/file:/app kgodzisz/shachecksum file-name file-checksum</code><br /><br />

<p><strong>Description of the options used in the commands:</strong></p>
<p><code>--rm</code> - the container will automatically be removed after exiting;</p>
<p><code>-v</code> - path to the folder where the file for which you want to compare the checksum is located. host directory : container working directory;</p> 
<p><code>shachecksum</code> - the name of the created image that we want to use;</p>
<p><code>kgodzisz/shachecksum</code> - the address to the image on the DockerHub platform.</p><br /><br />

<p><strong>Blog:</strong> https://dockeryzacjaswiata.pl</p>
<p><strong>Docker Hub:</strong> https://hub.docker.com/r/kgodzisz/shachecksum</p>
