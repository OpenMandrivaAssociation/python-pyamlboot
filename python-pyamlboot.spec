Name:		python-pyamlboot
Version:	1.0.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/pyamlboot/pyamlboot-%{version}.tar.gz
Summary:	Amlogic SoC USB Boot utility
URL:		https://pypi.org/project/pyamlboot/
License:	Apache 2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Amlogic SoC USB Boot utility

%prep
%autosetup -p1 -n pyamlboot-%{version}

%build
%py_build

%install
%py_install

mkdir -p %{buildroot}%{_prefix}/lib/udev/rules.d
cat >%{buildroot}%{_prefix}/lib/udev/rules.d/70-amlogic_khadas.rules <<'EOF'
# khadas vim3 initial flashing
# idVendor=1b8e, idProduct=c003
SUBSYSTEM=="usb", ATTR{idVendor}=="1b8e", ATTR{idProduct}=="c003", MODE="0660", TAG+="uaccess"

# khadas vim3 fastboot (initial bootloader)
# idVendor=1b8e, idProduct=fada,
SUBSYSTEM=="usb", ATTR{idVendor}=="1b8e", ATTR{idProduct}=="fada", MODE="0660", TAG+="uaccess"

# khadas vim3 adb
SUBSYSTEM=="usb", ATTR{idVendor}=="18d1", ATTR{idProduct}=="4e40", MODE="0660", TAG+="uaccess"
EOF

%files
%{_bindir}/*
%{py_sitedir}/files
%{py_sitedir}/pyamlboot
%{py_sitedir}/pyamlboot-*.*-info
%{_prefix}/lib/udev/rules.d/70*
