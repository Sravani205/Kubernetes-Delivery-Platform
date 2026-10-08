FROM jenkins/jenkins:lts-jdk17
USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates curl gnupg python3 python3-venv python3-pip \
 && install -m 0755 -d /etc/apt/keyrings \
 && curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc \
 && chmod a+r /etc/apt/keyrings/docker.asc \
 && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo $VERSION_CODENAME) stable" > /etc/apt/sources.list.d/docker.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends docker-ce-cli \
 && ARCH=$(dpkg --print-architecture) \
 && curl -fsSLo /usr/local/bin/kubectl "https://dl.k8s.io/release/$(curl -fsSL https://dl.k8s.io/release/stable.txt)/bin/linux/${ARCH}/kubectl" \
 && chmod +x /usr/local/bin/kubectl \
 && curl -fsSL "https://get.helm.sh/helm-v3.16.2-linux-${ARCH}.tar.gz" | tar -xz -C /tmp \
 && mv "/tmp/linux-${ARCH}/helm" /usr/local/bin/helm \
 && rm -rf /var/lib/apt/lists/* "/tmp/linux-${ARCH}"
USER jenkins
