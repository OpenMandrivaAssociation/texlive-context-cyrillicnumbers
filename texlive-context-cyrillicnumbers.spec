Name:		texlive-context-cyrillicnumbers
Version:	47085
Release:	2
Summary:	Write numbers as cyrillic glyphs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-cyrillicnumbers
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-cyrillicnumbers.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-cyrillicnumbers.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The package extends Context's system of number conversion, by
adding numeration using cyrillic letters.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-cyrillicnumbers.xml
%{_texmfdistdir}/tex/context/third/cyrillicnumbers
%doc %{_texmfdistdir}/doc/context/third/cyrillicnumbers

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
