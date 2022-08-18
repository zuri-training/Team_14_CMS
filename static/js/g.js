var editor = grapesjs.init({
  container : '#gjs',
  // Get the content for the canvas directly from the element
  // As an alternative we could use: `components: '<h1>Hello World Component!</h1>'`,
  fromElement: true,
  // Size of the editor
  width: 'auto',
  // Disable the storage manager for the moment
  storageManager: false,
  // Avoid any default panel
  panels: { defaults: [] },
  plugins: ['gjs-preset-webpage'],
  pluginsOpts: {
      'gjs-preset-webpage': {
      'blocks': ['link-block', 'quote', 'text-basic'],
      'modalImportTitle': 'Import',
      'modalImportButton': 'Import',
      'modalImportLabel': '',
      'modalImportContent': '',
      'importViewerOptions': {},
      'textCleanCanvas': 'Are you sure to clean the canvas?',
      'showStyleOnChange': true,
      // 'textGeneral': 'General';
      // 'textLayout': 'Layout',
      // 'textTypography': 'Typography',
      // 'textDecorations': 'Decorations',
      // 'textExtra': 'Extra',
      // 'customStyleManager': [],
    }
  }
});