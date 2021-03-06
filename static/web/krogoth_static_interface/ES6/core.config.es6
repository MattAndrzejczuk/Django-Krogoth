/*
GET   http://localhost:8000/global_static_text/load_static_text_readonly/core.config.es6
 */
(function () {
	'use strict';

	angular
		.module('app.core')
		.config(config);

	/** @ngInject */
	function config($ariaProvider, $logProvider, msScrollConfigProvider, fuseConfigProvider) {
		// Enable debug logging
		$logProvider.debugEnabled(true);

		/*eslint-disable */

		// ng-aria configuration
		$ariaProvider.config({
			tabindex: false
		});

		// Fuse theme configurations
		fuseConfigProvider.config({
			'disableCustomScrollbars': false,
			'disableCustomScrollbarsOnMobile': false,
			'disableMdInkRippleOnMobile': false
		});

		// msScroll configuration
		msScrollConfigProvider.config({
			wheelPropagation: true
		});

		/*eslint-enable */
	}
})();