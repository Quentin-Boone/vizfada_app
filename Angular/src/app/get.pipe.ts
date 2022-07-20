import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'get'
})
export class GetPipe implements PipeTransform {

  transform(obj: Object | undefined | string, key: string): Object | string {
    if (typeof(obj) === 'object' && obj !== null && key in obj) {
      let typeobj = typeof(obj[key]);
        if (typeobj === 'string') {
          return obj[key];
        } else {
          return new Object(obj[key]);
        }
    } else {
      return '';
    }
  }

}
