Summary:	A tool for KDE to access your applications/documents/bookmarks quickly
Summary(pl):	Narzêdzie dla KDE pozwalaj±ce na szybki dostêp do aplikacji/dokumentów/zak³adek
Name:		katapult
Version:	0.3.1.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/katapult/%{name}_%{version}.orig.tar.gz
# Source0-md5:	09ef2951e6e861b32fc63121e281f1da
URL:		http://wiki.thekatapult.org.uk/Home
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Katapult is a KDE application that gives you faster access to your
applications, bookmarks, and more! It is plugin-based and can launch
anything it has a plugin for. Its plugin-driven appearance is
completely customizable. Katapult was inspired by Quicksilver for OS
X, and it is written in C++.

%description -l pl
Katapult jest aplikacj± dla KDE, która umo¿liwia szybszy dostêp do
aplikacji, zak³adek, i wielu innych. Posiada modularn± budowê i mo¿e
uruchamiaæ wszystko, do czego posiada odpowiedni± wtyczkê. Dziêki temu
mo¿e byæ w du¿ym stopniu dostosowany do potrzeb u¿ytkownika. Aplikacja
jest wzorowana na Quicksilver dla OS X. Jest napisana w C++.

%prep
%setup -q

%build
%configure \
	--with-qt-libraries=%{_libdir}/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unnecessary
rm -rf $RPM_BUILD_ROOT{%{_datadir}/doc,%{_libdir}/*.la,%{_iconsdir}/*/scalable}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so*
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/*/*x*/*/*.png
%{_datadir}/services/katapult_*
%{_datadir}/servicetypes/katapult*
