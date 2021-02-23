vm.codeIDEStyle = [
    'FreeMono',
    'JMH Typewriter mono Black Under',
    'Droid Sans Mono',
    'JMH Typewriter mono',
    'NovaMono',
    'NK57 Monospace Eb',
    'NK57 Monospace Sc Rg',
    'NK57 Monospace Sc Lt',
    'NK57 Monospace Sc Eb',
    'BPmono',
    'JMH Typewriter mono Cross',
    'JMH Typewriter mono Fine Over',
    'JMH Typewriter mono Over',
    'NK57 Monospace Cd Sb',
    'NK57 Monospace Se Lt',
    'NK57 Monospace Ex Bk',
    'NK57 Monospace Sb',
    'Bitstream Vera Sans Mono',
    'Liberation Mono',
    'Ubuntu Mono',
    'FreeSans',
    'NK57 Monospace Ex Sb',
    'NK57 Monospace Se Bk',
    'JMH Typewriter mono Black Over',
    'NK57 Monospace Se Eb',
    'Anonymous Pro',
    'NinePin',
    'NK57 Monospace Cd Lt',
    'NK57 Monospace Ex Eb',
    'Source Code Pro',
    'Digital-7',
    'Inconsolata',
    'JMH Typewriter mono Fine Under',
    'Share Tech Mono',
    'NK57 Monospace Se Rg',
    'Courier Prime Code',
    'Digital-7 Mono',
    'CamingoCode',
    'Hack',
    'Fira Mono',
    'Unispace',
    'BPmonoStencil',
    'NK57 Monospace Ex Rg',
    'HydrogenType',
    'NK57 Monospace Se Sb',
    'Dotrice',
    'NK57 Monospace Cd Rg',
    'Larabiefont Rg',
    'Anonymous',
    'NK57 Monospace Lt',
    'NK57 Monospace Sc Bk',
    'NK57 Monospace Cd Bk',
    'Fantasque Sans Mono',
    'JMH Typewriter mono Fine',
    'NK57 Monospace Cd Eb',
    'JMH Typewriter mono Fine Cross',
    'JMH Typewriter mono Black Cross',
    'Sometype Mono',
    'FreeSerif',
    'JMH Typewriter mono Under',
    'NK57 Monospace Bk',
    'NK57 Monospace Rg',
    'NK57 Monospace Sc Sb',
    'NK57 Monospace Ex Lt'
];



vm.sizes = [1,2,3,4,5,6,7,8,9,10,11]

vm.uniqueArray = [];

for (let oldName of vm.codeIDEStyle) {
	let isUnique = true;
	for (let finalName of vm.uniqueArray) {
		if (finalName === oldName) {
			isUnique = false;
		}
	}
	if (isUnique) {
		vm.uniqueArray.push(oldName);
	}
}

vm.reloadSavedFonts = reloadSavedFonts;
function reloadSavedFonts() {
	$log.info("SAVING editorFontSize " + vm.size);
	$cookies.put('editorFontSize', vm.size);
	$log.info("SAVING editorFontType " + vm.codeFont);
	$cookies.put('editorFontType', vm.codeFont);
    vm.size = '7';
}

vm.loadFontSettingsCookies = loadFontSettingsCookies;

function loadFontSettingsCookies() {
	if ($cookies.get('editorFontSize')) {
		$log.info("USING FONT SIZE FROM COOKIES..."+$cookies.get('editorFontSize'));
		vm.size = $cookies.get('editorFontSize');
	} else {
		$log.info("USING DEFAULT FONT SIZE FROM COOKIES...");
		vm.size = '6';
	}

	if ($cookies.get('editorFontType')) {
		$log.info("USING FONT TYPEFACE FROM COOKIES..."+$cookies.get('editorFontType'));
		vm.codeFont = vm.uniqueArray[parseInt($cookies.get('editorFontType'))];
	} else {
		$log.info("USING DEFAULT TYPEFACE FROM COOKIES...");
		vm.codeFont = vm.uniqueArray[0];
	}
}