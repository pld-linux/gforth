Summary:	GNU Forth Language
Summary(pl.UTF-8):	Kompilator GNU Forth
Name:		gforth
Version:	0.7.3
Release:	1
License:	GPL v3+
Group:		Development/Languages
Source0:	http://ftp.gnu.org/gnu/gforth/%{name}-%{version}.tar.gz
# Source0-md5:	ff484391e5cdf405867fcf96341820ab
Patch0:		%{name}-info.patch
Patch1:		%{name}-opt.patch
URL:		http://gnu.org/software/gforth/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	ffcall-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	.*%{_libdir}/gforth/%{version}/libcc-named/.*

%description
Gforth is a fast and portable implementation of the ANS Forth
language. It works nicely with the Emacs editor, offers some nice
features such as input completion and history and a powerful locals
facility, and it even has (the beginnings of) a manual. Gforth employs
traditional implementation techniques: its inner interpreter is
indirect or direct threaded. Gforth is distributed under the GNU
General Public License.

%description -l pl.UTF-8
Gforth jest szybką i przenośną implementacją języka ANS Forth. Dobrze
współpracuje z edytorem Emacs, oferując takie cechy jak dopełnianie i
historię wprowadzania ciągów znaków, ma także zaczątki podręcznika.
Gforth wykorzystuje tradycyjne techniki implementacji: jego wewnętrzny
interpreter jest pośrednio lub bezpośrednio wątkowany. Gforth jest
rozpowszechniany na Powszechnej Licencji Publicznej GNU.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__rm} doc/*.info*

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%{__make} info

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gforth/%{version}/libcc-named/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS NEWS NEWS.vmgen README README.vmgen ToDo
%attr(755,root,root) %{_bindir}/gforth*
%attr(755,root,root) %{_bindir}/vmgen*
%dir %{_libdir}/gforth
%dir %{_libdir}/gforth/%{version}
%dir %{_libdir}/gforth/%{version}/libcc-named
%attr(755,root,root) %{_libdir}/gforth/%{version}/libcc-named/*.so*
%attr(755,root,root) %{_libdir}/gforth/%{version}/gforth-ditc
%{_libdir}/gforth/%{version}/gforth.fi
%dir %{_libdir}/gforth/site-forth
%{_includedir}/gforth
%{_infodir}/gforth.info*
%{_infodir}/vmgen.info*
%{_mandir}/man1/gforth.1*
%{_datadir}/gforth
