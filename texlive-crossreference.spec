Name:		texlive-crossreference
Version:	15878
Release:	2
Summary:	Crossreferences within documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/crossreference
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/crossreference.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines cross-references (essentially 'grand' label
references), which may be listed in a table of cross-
references.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/crossreference/crossreference.sty
%doc %{_texmfdistdir}/doc/latex/crossreference/README
%doc %{_texmfdistdir}/doc/latex/crossreference/crossreference.pdf
%doc %{_texmfdistdir}/doc/latex/crossreference/xrefexample.tex
#- source
%doc %{_texmfdistdir}/source/latex/crossreference/crossreference.drv
%doc %{_texmfdistdir}/source/latex/crossreference/crossreference.dtx
%doc %{_texmfdistdir}/source/latex/crossreference/crossreference.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
