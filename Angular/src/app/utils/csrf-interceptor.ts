import { Injectable } from '@angular/core';
import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest, HttpXsrfTokenExtractor } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable()
export class CsrfInterceptor implements HttpInterceptor {
    constructor(private tokenExtractor: HttpXsrfTokenExtractor) {
    }

    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        const csrfHeaderName = "HTTP_X_CSRF_TOKEN";
        let csrfToken = this.tokenExtractor.getToken() as string;
        console.log("csrf token", csrfToken);
        if (csrfToken !== null && !req.headers.has(csrfHeaderName)) {
            req = req.clone({ headers: req.headers.set(csrfHeaderName, csrfToken)})
        }
        return next.handle(req)
    }
}