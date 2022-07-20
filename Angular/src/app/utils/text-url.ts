export interface TextUrl {
  text: string;
  url: string
}

export interface Ontology extends TextUrl {
  ontologyTerms: string;
}

export interface File extends TextUrl {
  filename: string;
}

export interface TextUnit extends TextUrl {
  unit: string;
}

export interface Article extends TextUrl {
  title: string;
  jounal: string;
  year: number;
}

export interface Organization extends TextUrl {
  name: string;
  role: string;
}

export class CastTextUrl {
  
  private texturl: TextUrl | Ontology | Article | File | TextUnit | Organization | Object;
  
  constructor(object: Object) {
    this.texturl = this.cast(object);
  }
  
  public cast(object: Object): TextUrl | Ontology | Article | File | TextUnit | Organization | Object {
    let keys = Object.keys(object);
    if ('text' in keys && 'url' in keys) {
      if ('ontologyTerms' in keys) {
        return object as Ontology;
      } else if ('filename' in keys) {
        return object as File;
      } else if ('role' in keys) {
        return object as Organization;
      } else if ('unit' in keys) {
        return object as TextUnit;
      } else if ('title' in keys) {
        return object as Article;
      } else {
        return object as TextUrl;
      }
    } else {
      return object;
    }
  }
  
  public get(): TextUrl | Ontology | Article | File | TextUnit | Organization | Object {
    return this.texturl;
  }
  
}

export interface DataJSON {
  name: string;
  type: string;
  mtime: string;
  size: number;
  url: string;
  parent: string;
  download: string;
}

export interface Folder {
  name: string;
  type: string;
  expanded: boolean;
  content: (Folder | DataJSON)[];
}
