import { Component } from '@angular/core';
<<<<<<< HEAD
import { Categories } from './categories';
=======
>>>>>>> dfa4b5b1c40a1a5bb10ccf20916a5c82b2c6b7ae

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
<<<<<<< HEAD
  categories = Categories;
  show = false;
  categoryName = "";
  categoryClick(name: string) {
    if(this.categoryName == name) {
      this.show = false;
      this.categoryName = "";
    }
    else {
      this.show = true;
      this.categoryName = name;
    }
  }
=======
>>>>>>> dfa4b5b1c40a1a5bb10ccf20916a5c82b2c6b7ae
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/