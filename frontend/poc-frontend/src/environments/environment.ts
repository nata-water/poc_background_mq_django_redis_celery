// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  apiServer: 'http://127.0.0.1:8000',
  apiRoot: 'xxx_api',
  // BinaryResource取得用API
  apiGetBinaryResources: 'v1/binary_resources',
  apiGetBinaryHeavyResources: 'v1/binary_heavy_resources',
  // ParseResult取得用API
  apiGetParseResults: 'v1/parse_results',
  // BinaryResource抽出実行API
  apiDoParseResource: 'v1/do_parse_resource',
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.
