# TODO:
# - look at MPI support - doesn't work with lam for me :/
# - use system libffi
Summary:	FreeMat - an environment for rapid engineering and scientific processing
Summary(pl):	FreeMat - ¶rodowisko do szybkiego przetwarzania in¿ynieryjnego i naukowego
Name:		FreeMat
Version:	1.09
Release:	2
License:	MIT
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/freemat/%{name}-%{version}.tar.gz
# Source0-md5:	87b9615d9071ccc3073fd3fe5d31bd6e
Source1:	%{name}.desktop
URL:		http://freemat.sourceforge.net
BuildRequires:	automake
BuildRequires:	blas-devel
BuildRequires:	fltk-devel
BuildRequires:	gcc-g77
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FreeMat is a free environment for rapid entineering and scientific
prototyping and data processing. It is similar to commercial systems
such as MATLAB from Mathworks, and IDL from Research Systems, but is
Open Source. FreeMat includes several novel features such as a
codeless interface to external C/C++/FORTRAN code,
parallel/distributed algorithm development (via MPI), and plotting and
visualiation capabilities.

%description -l pl
FreeMat jest darmowym ¶rodowiskiem do szybkiego przetwarzania
prototypów i danych dla in¿ynierów i naukowców. Jest podobny do
komercyjnych systemów takich jak MATLAB z Mathworks i IDL z Research
Group, ale na licencji Open Source. FreeMat cechuje siê miêdzy innymi
bezkodowym interfejsem do zewnêtrznego kodu C/C++/FORTRAN,
równoleg³ym/rozproszonym algorytmem obliczeñ (poprzez MPI), oraz
rysowaniem i wy¶wietlaniem mo¿liwo¶ci.

%prep
%setup -q

%build
cp -f %{_datadir}/automake/config.sub .
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
CXXFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
%configure \
	--with-ncurses

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_infodir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
