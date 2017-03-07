FROM lasote/conangcc48
ARG ruby_version=2.4.0
MAINTAINER Michel Estermann <estermann.michel@gmail.com>

USER root
ENV RBENV_ROOT /home/conan/.rbenv
ENV PATH $RBENV_ROOT/shims:$RBENV_ROOT/plugins/ruby-build/bin:$RBENV_ROOT/bin:$PATH
RUN apt-get update && apt-get install -y libreadline-dev libssl-dev zlib1g-dev

USER conan
# install rbenv
RUN cd
RUN git clone git://github.com/sstephenson/rbenv.git $RBENV_ROOT
RUN git clone git://github.com/sstephenson/ruby-build.git $RBENV_ROOT/plugins/ruby-build
RUN echo 'export PATH="$RBENV_ROOT/plugins/ruby-build/bin:$RBENV_ROOT/bin:$PATH"' >> ~/.bashrc
RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc

# install ruby version (global)
RUN bash -c "rbenv install -s $ruby_version && rbenv global $ruby_version && rbenv rehash"
RUN bash -c "gem install bundler --no-document"
