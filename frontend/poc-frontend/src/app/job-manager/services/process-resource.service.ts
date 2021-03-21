import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, of } from 'rxjs';
import { BinaryResource } from '../interfaces/BinaryResource';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment as env } from '../../../environments/environment';
import { catchError, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class ProcessResourceService {
  // 処理対象ファイルの状態管理用オブジェクト
  private _binaryResources$ = new BehaviorSubject<BinaryResource[]>([]);

  // 処理対象ファイル取得APIエンドポイント
  private _apiGetBinaryResources = `${env.apiServer}/${env.apiRoot}/${env.apiGetBinaryResources}`;

  // 対象ファイルDBテーブル格納処理APIエンドポイント
  private _apiDoParseResource = `${env.apiServer}/${env.apiRoot}/${env.apiDoParseResource}/`;

  private _httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  };

  // コンポーネント公開用の処理対象ファイル状態
  get binaryResources$(): Observable<BinaryResource[]> {
    return this._binaryResources$.asObservable();
  }

  constructor(private http: HttpClient) {}

  /***
   * 処理対象ファイルを取得するAPIを実行します
   */
  fetchBinaryResources(): void {
    this.http
      .get(this._apiGetBinaryResources, {
        withCredentials: true,
      })
      // .pipe(map((resp) => resp.data))
      .subscribe((resp: BinaryResource[]) => {
        const binaryResources: BinaryResource[] = [];
        resp.forEach((resource) => {
          binaryResources.push(resource);
        });
        this._binaryResources$.next(binaryResources);
      });
  }

  /***
   *  対象ファイルをDBテーブルに格納する処理APIを実行します
   */
  doParseResource(resourceId: string): Observable<any> {
    const requestParam = { resource_id: resourceId };
    return this.http
      .post<string>(this._apiDoParseResource, requestParam, this._httpOptions)
      .pipe(
        tap((_) => {}),
        catchError(this.handleError<any>('doParseResource'))
      );
  }

  private handleError<T>(operation = 'operation', result?: T): any {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }
}
