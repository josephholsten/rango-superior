%global debug_package %{nil}
%global _revision 04d0b02

Name:           fzf
Version:        0.34.0
Release:        1%{?dist}
Summary:        A command-line fuzzy finder written in Go

License:        MIT
URL:            https://github.com/junegunn/fzf
Source0:        https://github.com/junegunn/fzf/archive/%{version}.tar.gz

BuildRequires:  gcc git make
BuildRequires:  golang

%description
fzf is a general-purpose command-line fuzzy finder.

It's an interactive Unix filter for command-line that can be used with any
list; files, command history, processes, hostnames, bookmarks, git commits,
etc.

%prep
%autosetup

%build
make FZF_VERSION=%{version} FZF_REVISION=%{_revision} all install

%check
make FZF_VERSION=%{version} FZF_REVISION=%{_revision} test

%install
mkdir -p %{buildroot}%{_bindir}
install -Dpm 755 -t %{buildroot}%{_bindir} bin/%{name}
install -Dpm 755 -t %{buildroot}%{_bindir} bin/%{name}-tmux

mkdir -p %{buildroot}%{_mandir}/man1
install -Dpm 644 -t %{buildroot}%{_mandir}/man1 man/man1/%{name}.1
install -Dpm 644 -t %{buildroot}%{_mandir}/man1 man/man1/%{name}-tmux.1

mkdir -p %{buildroot}%{_datadir}/%{name}
install -Dpm 644 shell/completion.zsh   %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dpm 644 shell/completion.bash  %{buildroot}%{_datadir}/bash-completion/completions/%{name}

install -Dpm 644 -t %{buildroot}%{_datadir}/%{name} shell/key-bindings.bash
install -Dpm 644 shell/key-bindings.zsh   %{buildroot}%{_datadir}/zsh/site-functions/_%{name}-key-bindings
install -Dpm 644 shell/key-bindings.fish  %{buildroot}%{_datadir}/fish/vendor_functions.d/%{name}_key_bindings.fish

mkdir -p %{buildroot}%{_datadir}/vim/vimfiles/{doc,plugin}
install -Dpm 644 -t %{buildroot}%{_datadir}/vim/vimfiles/doc    doc/%{name}.txt
install -Dpm 644 -t %{buildroot}%{_datadir}/vim/vimfiles/plugin plugin/%{name}.vim

%files
%license LICENSE
%doc ADVANCED.md CHANGELOG.md README.md README-VIM.md doc/%{name}.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-tmux
%{_mandir}/man1/%{name}.1
%{_mandir}/man1/%{name}-tmux.1
%{_datadir}/%{name}/*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_functions.d/%{name}_key_bindings.fish
%{_datadir}/vim/vimfiles/doc/%{name}.txt
%{_datadir}/vim/vimfiles/plugin/%{name}.vim
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}-key-bindings


%changelog
* Fri Oct 21 2022 josephholsten - 0.34.0-1
- Release 0.34.0
