Summary:     GNU Forth Language
Summary(pl): Kompilator GNU Forth 
Name:        gforth
Version:     0.3.0
Release:     2
Copyright:   GPL
Group:       Languages
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz 
Patch0:      gforth-makefile.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Gforth is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history and a powerful locals
facility, and it even has (the beginnings of) a manual. Gforth employs
traditional implementation techniques: its inner innerpreter is
indirect or direct threaded.  Gforth is distributed under the GNU
General Public license (see COPYING).

%description -l pl
Gforth jest szybk± i przenoszaln± implementacj± jêzyka ANS Forth.
Dobrae wspólpracuje z edytorem Emacs oferuj±c takie cechy jak kompletowanie
i historiê wprowadzania ci±gów znaków.

%prep
%setup -q
%patch0 -p1

%build
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/gforth.info*

%post
/sbin/install-info %{_infodir}/gforth.info.gz /usr/info/dir \
--section "Programming:" --entry \
"* Gforth: (gforth.info).                       The GNU ANS Forth."

%preun
/sbin/install-info --delete %{_infodir}/gforth.info.gz /usr/info/dir \
--section "Programming:" --entry \
"* Gforth: (gforth.info).                       The GNU ANS Forth."


%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644,root,root,755)
%doc README TAGS BUGS ToDo
%attr(755,root,root) %{_bindir}/*
%{_libdir}/gforth
%{_infodir}/*info*
%{_mandir}/man1/*
%{_datadir}/gforth

%changelog
* Sun Nov 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3.0-2]
- added using $RPM_OPT_FLAGS during compile,
- added %post, %preun with {un}registering info pages,
- removed making htm and ps documentation (it can be generatred from
  info pages by onyone in anytime).

* Wed Sep 23 1998 Wojciech "Sas" Ciêciwa <cieciwa@zarz.agh.edu.pl>
  [0.3.0-1]
- Building RPM.
