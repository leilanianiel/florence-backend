(this.webpackJsonpflorence=this.webpackJsonpflorence||[]).push([[0],{116:function(e,t,n){},118:function(e,t,n){},120:function(e,t,n){},121:function(e,t,n){},144:function(e,t,n){},147:function(e,t,n){},150:function(e,t,n){"use strict";n.r(t);var c=n(0),a=n.n(c),r=n(13),i=n.n(r),o=(n(116),n(10)),s=n.n(o),d=n(15),u=n(12),l=n(44),j=n(95),b=n(203),O=n(191),f=n(188),p=n(205),m=n(202),v=n(211),x=n(90),h=n.n(x),_=n(91),S=n.n(_),g=n(92),y=n.n(g),E=n(93),C=n.n(E),T=(n(118),n.p+"static/media/About Florence.1e02f1e5.png"),N=n.p+"static/media/Copy of Copy of Florence.b31350a6.png",P=n(2);var w=function(){return Object(P.jsxs)("div",{className:"About",children:[Object(P.jsx)("img",{className:"about florence",src:T,alt:"Florence the invetory of the electic fridge."}),Object(P.jsx)("img",{className:"about florence",src:N,alt:"Florence the invetory of the electic fridge."})]})},R=(n(120),n(121),n.p+"static/media/Copy of Florence (9).721f04aa.png");var D=function(){return Object(P.jsx)("div",{className:"Home",logo:!0,children:Object(P.jsx)("img",{className:"about florence",src:R,alt:"logo"})})},A=n(184),I=(n(69),Object({NODE_ENV:"production",PUBLIC_URL:"",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_API_ENDPOINT||window.location.origin);var k=function(){return Object(P.jsxs)("div",{className:"LogIn",children:[Object(P.jsx)(A.a,{className:"btn",variant:"contained",color:"primary",href:"".concat(I,"/login"),children:"Login"}),Object(P.jsx)(A.a,{className:"btn",variant:"contained",color:"secondary",href:"".concat(I,"/register"),children:"Register"})]})},F=n(16),L=n.n(F),H=(n(144),n(145),n(192)),B=n(195),K=n(193),W=n(194),U=n(200),V=n(208),z=n(32),q=n.n(z),M=(n(147),n(88)),J=n.n(M),Y=n(187),G=n(189),Q=n(190),X=n(87),Z=n.n(X),$=n(89),ee=n.n($),te=n(196),ne=Object({NODE_ENV:"production",PUBLIC_URL:"",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_API_ENDPOINT||window.location.origin,ce=Object(Y.a)((function(e){return{appBar:{position:"relative"},title:{marginLeft:e.spacing(2),flex:1}}}));function ae(e){var t=ce(),n=Object(c.useState)([]),a=Object(u.a)(n,2),r=a[0],i=a[1],o=Object(c.useState)([]),l=Object(u.a)(o,2),j=l[0],b=l[1],p=function(){var e=Object(d.a)(s.a.mark((function e(t){var n;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,L.a.post("".concat(ne,"/item/").concat(t,"/decrease_count"));case 2:n=e.sent,console.log(n),v();case 5:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),m=function(){var e=Object(d.a)(s.a.mark((function e(t){var n;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,L.a.delete("".concat(ne,"/item/").concat(t));case 2:n=e.sent,console.log(n),v();case 5:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}();function v(){return x.apply(this,arguments)}function x(){return(x=Object(d.a)(s.a.mark((function t(){var n,c;return s.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,L.a.get("".concat(ne,"/fridge/").concat(e.fridgeId,"/items"));case 2:n=t.sent,c=(c=n.data.filter((function(t){return e.expirySoon?q()(t.expiration).diff(q()(),"days")<3:t.product_id===e.selectedProduct}))).sort((function(e,t){return q()(e.expiration).diff(q()(t.expiration))})),console.log(c),i(c);case 7:case"end":return t.stop()}}),t)})))).apply(this,arguments)}return Object(c.useEffect)((function(){function e(){return(e=Object(d.a)(s.a.mark((function e(){var t;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,L.a.get("".concat(ne,"/product"));case 2:t=e.sent,b(t.data);case 4:case"end":return e.stop()}}),e)})))).apply(this,arguments)}!function(){e.apply(this,arguments)}()}),[]),Object(c.useEffect)((function(){0!==j.count&&v()}),[j,e.fridgeId,e.selectedProduct]),Object(P.jsxs)("div",{children:[Object(P.jsx)(f.a,{className:t.appBar,color:"secondary",children:Object(P.jsxs)(G.a,{children:[Object(P.jsx)(Q.a,{edge:"start",color:"inherit",onClick:e.handleClose,"aria-label":"close",children:Object(P.jsx)(Z.a,{})}),Object(P.jsx)(O.a,{variant:"h6",className:t.title,children:"Items"})]})}),Object(P.jsx)("div",{className:"itemContainer",children:r.map((function(e){var t=j.find((function(t){return t.id===e.product_id}));if(console.log(t),!t)return Object(P.jsx)(P.Fragment,{});var n=q()(e.expiration);return Object(P.jsxs)(H.a,{className:"item",children:[Object(P.jsxs)(K.a,{children:[Object(P.jsx)(O.a,{color:"textSecondary",gutterBottom:!0,children:t.name}),Object(P.jsx)(O.a,{color:"textSecondary",gutterBottom:!0,children:e.count}),Object(P.jsxs)(O.a,{color:"textSecondary",gutterBottom:!0,children:["Expires ",n.fromNow()]}),Object(P.jsx)(W.a,{className:"product-image",image:t.image,title:t.name})]}),Object(P.jsxs)(B.a,{children:[Object(P.jsx)(te.a,{onClick:function(){p(e.id)},color:"primary","aria-label":"add",size:"small",children:Object(P.jsx)(J.a,{})}),Object(P.jsx)(te.a,{onClick:function(){m(e.id)},color:"primary","aria-label":"add",size:"small",children:Object(P.jsx)(ee.a,{})})]})]})}))})]})}var re=n(197),ie=n(207),oe=n(204),se=n(210),de=n(24),ue=n.n(de),le=Object({NODE_ENV:"production",PUBLIC_URL:"",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_API_ENDPOINT||window.location.origin;var je=function(e){var t=Object(c.useState)(""),n=Object(u.a)(t,2),a=n[0],r=n[1],i=Object(c.useState)(-1),o=Object(u.a)(i,2),l=o[0],j=o[1],b=Object(c.useState)(""),O=Object(u.a)(b,2),f=O[0],p=O[1],m=Object(c.useState)(""),v=Object(u.a)(m,2),x=v[0],h=v[1],_=Object(c.useState)(!1),S=Object(u.a)(_,2),g=S[0],y=S[1],E=function(){ue.a.stop(),y(!1)},C=function(){var t=Object(d.a)(s.a.mark((function t(n){var c;return s.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return n.preventDefault(),c={name:a,category_id:parseInt(l),image:f},x&&(c.barcode=x),t.next=5,L.a.post("".concat(le,"/product"),c);case 5:t.sent,e.getProducts(),r(""),h(""),p(""),j(-1);case 11:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),T=function(){var e=Object(d.a)(s.a.mark((function e(t){return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:y(!0),ue.a.init({inputStream:{name:"Live",type:"LiveStream",target:"#productBarcode"},decoder:{readers:["code_128_reader","ean_reader","code_39_reader","code_39_vin_reader","upc_e_reader","codabar_reader","2of5_reader","code_93_reader"]}},(function(e){if(e)console.log(e);else{console.log("Initialization finished. Ready to start");var t=ue.a.onDetected((function(e){console.log(e),h(e.codeResult.code),ue.a.offDetected(t),E()}));ue.a.start()}}));case 2:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}();return Object(P.jsx)(re.a,{children:Object(P.jsxs)("form",{className:"form",onSubmit:C,children:[Object(P.jsx)("label",{children:"Add New Product"}),Object(P.jsx)("div",{children:Object(P.jsx)(ie.a,{variant:"outlined",type:"text",name:"name",placeholder:"Food Name",value:a,onChange:function(e){return r(e.target.value)}})}),Object(P.jsx)("div",{children:Object(P.jsx)(ie.a,{variant:"outlined",type:"url",name:"Image",placeholder:"Paste image URL",value:f,onChange:function(e){return p(e.target.value)}})}),Object(P.jsxs)("div",{children:[Object(P.jsx)(A.a,{variant:"contained",color:"primary",onClick:T,children:"Scan barcode"}),Object(P.jsx)("div",{className:"cover ".concat(g?"visible":""),onClick:E,children:Object(P.jsx)("div",{id:"productBarcode",className:"viewport"})})]}),Object(P.jsx)("div",{children:Object(P.jsx)(ie.a,{variant:"outlined",type:"text",name:"Barcode",placeholder:"Barcode",value:x})}),Object(P.jsx)("div",{children:Object(P.jsxs)(oe.a,{value:l,onChange:function(e){return j(e.target.value)},displayEmpty:!0,children:[Object(P.jsx)(se.a,{value:-1,disabled:!0,children:"Select Category"}),e.categories&&e.categories.map((function(e){return Object(P.jsx)(se.a,{value:e.id,children:e.name},e.id)}))]})}),Object(P.jsx)("div",{className:"space",children:Object(P.jsx)(A.a,{type:"submit",variant:"contained",color:"primary",children:"Submit"})})]})})},be=Object({NODE_ENV:"production",PUBLIC_URL:"",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_API_ENDPOINT||window.location.origin;var Oe=function(e){var t=Object(c.useState)(""),n=Object(u.a)(t,2),a=n[0],r=n[1],i=Object(c.useState)(-1),o=Object(u.a)(i,2),l=o[0],j=o[1],b=Object(c.useState)(""),O=Object(u.a)(b,2),f=O[0],p=O[1],m=Object(c.useState)(""),v=Object(u.a)(m,2),x=(v[0],v[1]),h=Object(c.useState)(!1),_=Object(u.a)(h,2),S=_[0],g=_[1],y=function(){ue.a.stop(),g(!1)},E=function(){var t=Object(d.a)(s.a.mark((function t(n){var c,i;return s.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return n.preventDefault(),c={count:parseInt(a),product_id:parseInt(l),fridge_id:e.fridgeId},(i=parseInt(f))&&(c.expiration=i),t.next=6,L.a.post("".concat(be,"/item"),c);case 6:t.sent,e.getItems(),p(""),j(-1),x(""),r("");case 12:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),C=function(){var t=Object(d.a)(s.a.mark((function t(n){return s.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:g(!0),ue.a.init({inputStream:{name:"Live",type:"LiveStream",target:"#itemBarcode"},decoder:{readers:["code_128_reader","ean_reader","code_39_reader","upc_e_reader","code_39_vin_reader","codabar_reader","2of5_reader","code_93_reader"]}},(function(t){if(t)console.log(t);else{console.log("Initialization finished. Ready to start");var n=ue.a.onDetected((function(t){console.log(t);var c=e.products.find((function(e){return e.barcode===t.codeResult.code}));c&&(ue.a.offDetected(n),j(c.id),y())}));ue.a.start()}}));case 2:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}();return Object(P.jsx)(re.a,{children:Object(P.jsxs)("form",{className:"form",onSubmit:E,children:[Object(P.jsx)("label",{children:"Add New Item"}),Object(P.jsxs)("div",{children:[Object(P.jsx)(A.a,{variant:"contained",color:"primary",onClick:C,children:"Scan barcode"}),Object(P.jsx)("div",{className:"cover ".concat(S?"visible":""),onClick:y,children:Object(P.jsx)("div",{id:"itemBarcode",className:"viewport"})})]}),Object(P.jsx)("div",{children:Object(P.jsxs)(oe.a,{value:l,onChange:function(e){return j(e.target.value)},displayEmpty:!0,children:[Object(P.jsx)(se.a,{value:-1,disabled:!0,children:"Select Product"}),e.products&&e.products.map((function(e){return Object(P.jsx)(se.a,{value:e.id,children:e.name},e.id)}))]})}),Object(P.jsx)("div",{children:Object(P.jsx)(ie.a,{variant:"outlined",type:"number",name:"count",placeholder:"Count",value:a,onChange:function(e){return r(e.target.value)}})}),Object(P.jsx)(ie.a,{variant:"outlined",type:"number",name:"expiration",placeholder:"Expiration",value:f,onChange:function(e){return p(e.target.value)}}),Object(P.jsx)("div",{className:"space",children:Object(P.jsx)(A.a,{type:"submit",variant:"contained",color:"primary",children:"Submit"})})]})})},fe=n.p+"static/media/Florence Logo.2695756b.png",pe=Object({NODE_ENV:"production",PUBLIC_URL:"",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_API_ENDPOINT||window.location.origin,me=Object({NODE_ENV:"production",PUBLIC_URL:"",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_TEST_USER||window.userId,ve=a.a.forwardRef((function(e,t){return Object(P.jsx)(U.a,Object(l.a)({direction:"up",ref:t},e))}));var xe=function(){var e=Object(c.useState)([]),t=Object(u.a)(e,2),n=t[0],a=t[1],r=Object(c.useState)(),i=Object(u.a)(r,2),o=i[0],l=i[1],j=Object(c.useState)(),b=Object(u.a)(j,2),f=b[0],p=b[1],m=Object(c.useState)(),v=Object(u.a)(m,2),x=v[0],h=v[1],_=Object(c.useState)([]),S=Object(u.a)(_,2),g=S[0],y=S[1],E=Object(c.useState)([]),C=Object(u.a)(E,2),T=C[0],N=C[1],w=Object(c.useState)(void 0),R=Object(u.a)(w,2),D=R[0],I=R[1],k=Object(c.useState)(!1),F=Object(u.a)(k,2),U=F[0],z=F[1],M=Object(c.useState)(!1),J=Object(u.a)(M,2),Y=J[0],G=J[1],Q=Object(c.useState)(),X=Object(u.a)(Q,2),Z=X[0],$=X[1],ee=function(){G(!0)},te=function(){var e=Object(d.a)(s.a.mark((function e(){var t;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,L.a.get("".concat(pe,"/recipes/"));case 2:t=e.sent,p(t.data);case 4:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),ne=function(){G(!1),h(),z(!1)},ce=function(e,t){return e.product.name.localeCompare(t.product.name)},re=function(e,t){return e.name.localeCompare(t.name)};function ie(){return oe.apply(this,arguments)}function oe(){return(oe=Object(d.a)(s.a.mark((function e(){var t;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,L.a.get("".concat(pe,"/product"));case 2:t=e.sent,y(t.data.sort(re));case 4:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function se(){return de.apply(this,arguments)}function de(){return(de=Object(d.a)(s.a.mark((function e(){var t,n,c,r,i,d,u;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,L.a.get("".concat(pe,"/fridge/").concat(o.fridge_id,"/items"));case 2:if(t=e.sent,n={},0,t.data.map((function(e){if(n[e.product_id])n[e.product_id].quantity+=e.count;else{var t=g.find((function(t){return t.id===e.product_id}));t&&(n[e.product_id]={quantity:e.count,product:t,item:e})}return e})),c=Object.values(n).filter((function(e){return q()(e.item.expiration).diff(q()(),"days")<3})),a(Object.values(n)),!(c.length>0)){e.next=23;break}if(r="Hey!",i=void 0,d=window.location.origin+fe,console.log(d),u={body:"You have ".concat(c.length," items expiring soon"),image:c[0].product.image,icon:d},"granted"!==Notification.permission){e.next=18;break}i=new Notification(r,u),e.next=22;break;case 18:return e.next=20,Notification.requestPermission();case 20:"granted"===e.sent&&(i=new Notification(r,u));case 22:i.onclick=function(){z(!0),ee()};case 23:N(Object.values(n).sort(ce));case 24:case"end":return e.stop()}}),e)})))).apply(this,arguments)}return Object(c.useEffect)((function(){if(void 0!==D&&0!==n.count&&0!==g.count){var e=n.filter((function(e){if(-1===D)return!0;var t=g.find((function(t){return t.id===e.item.product_id}));return!!t&&t.category_id===D}));N(e.sort(ce))}}),[g,D,n]),Object(c.useEffect)((function(){function e(){return(e=Object(d.a)(s.a.mark((function e(){var t,n;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,L.a.get("".concat(pe,"/customer/").concat(me));case 2:return t=e.sent,l(t.data),e.next=6,L.a.get("".concat(pe,"/category"));case 6:n=e.sent,$(n.data.sort(re));case 8:case"end":return e.stop()}}),e)})))).apply(this,arguments)}ie(),function(){e.apply(this,arguments)}()}),[]),Object(c.useEffect)((function(){o&&0!==g.length&&se()}),[o,g]),Object(P.jsxs)("div",{className:"MyFridge",children:[Object(P.jsxs)("div",{className:"btnParent",children:[Object(P.jsx)(A.a,{className:"btn",variant:"contained",onClick:function(){return I(-1)},color:-1===D?"secondary":"primary",children:"All Items"}),Object(P.jsx)(A.a,{className:"btn",variant:"contained",onClick:function(){z(!0),ee()},color:U?"secondary":"primary",children:"Expiring Soon"}),Object(P.jsx)(A.a,{size:"small",className:"btn",variant:"contained",onClick:function(){return I(4)},color:4===D?"secondary":"primary",children:"Dairy"}),Object(P.jsx)(A.a,{className:"btn",variant:"contained",onClick:function(){return I(3)},color:3===D?"secondary":"primary",children:"Meat"}),Object(P.jsx)(A.a,{className:"btn",variant:"contained",onClick:function(){return I(5)},color:5===D?"secondary":"primary",children:"Fruit"}),Object(P.jsx)(A.a,{className:"btn",variant:"contained",onClick:function(){return I(2)},color:2===D?"secondary":"primary",children:"Veggies"}),Object(P.jsx)(A.a,{className:"btn",variant:"contained",onClick:function(){return I(7)},color:7===D?"secondary":"primary",children:"Drinks"})]}),Object(P.jsx)("div",{className:"itemParent",children:T.map((function(e,t){var n=g.find((function(t){return t.id===e.item.product_id}));return n?Object(P.jsxs)(H.a,{className:"item",children:[Object(P.jsxs)(K.a,{children:[Object(P.jsx)(O.a,{color:"textSecondary",gutterBottom:!0,children:n.name}),Object(P.jsx)(O.a,{color:"textSecondary",gutterBottom:!0,children:e.quantity}),Object(P.jsx)(W.a,{className:"product-image",image:n.image,title:n.name})]}),Object(P.jsx)(B.a,{children:Object(P.jsx)(A.a,{size:"small",onClick:function(){ee(),h(n.id)},children:"show item"})})]},t):Object(P.jsx)(P.Fragment,{})}))}),Object(P.jsxs)("div",{children:[Object(P.jsx)("div",{className:"addProduct"}),Z&&Object(P.jsx)(je,{getProducts:ie,categories:Z}),o&&g&&Object(P.jsx)(Oe,{getItems:se,products:g,fridgeId:o.fridge_id}),Object(P.jsxs)("div",{children:[Object(P.jsx)("div",{children:f&&f.map((function(e){return Object(P.jsxs)("div",{children:[Object(P.jsx)("img",{src:e.image,alt:e.name}),Object(P.jsx)("div",{children:Object(P.jsx)("a",{href:e.url,rel:"noreferrer",target:"_blank",children:e.name})})]},e.name)}))}),Object(P.jsx)(A.a,{onClick:function(){te()},className:"btn recipes",variant:"contained",color:"secondary",children:"Find Recipes"})]}),o&&Object(P.jsx)(V.a,{fullScreen:!0,open:Y,onClose:ne,TransitionComponent:ve,children:Object(P.jsx)(ae,{handleClose:ne,fridgeId:o.fridge_id,selectedProduct:x,expirySoon:U})})]})]})},he=n(94),_e=n(201),Se=Object({NODE_ENV:"production",PUBLIC_URL:"",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_TEST_USER||window.userId,ge=Object({NODE_ENV:"production",PUBLIC_URL:"",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_API_ENDPOINT||window.location.origin,ye=Object(he.a)({palette:{primary:{main:"#FAC4C4"},secondary:{main:"#22783E"}}});function Ee(e){var t=e.children,n=e.value,c=e.index,a=Object(j.a)(e,["children","value","index"]);return Object(P.jsx)("div",Object(l.a)(Object(l.a)({role:"tabpanel",hidden:n!==c,id:"simple-tabpanel-".concat(c),"aria-labelledby":"simple-tab-".concat(c)},a),{},{children:n===c&&Object(P.jsx)(b.a,{p:3,children:Object(P.jsx)(O.a,{children:t})})}))}var Ce=function(){var e=a.a.useState(0),t=Object(u.a)(e,2),n=t[0],r=t[1],i=Object(c.useState)(),o=Object(u.a)(i,2),l=o[0],j=o[1];return Object(c.useEffect)((function(){function e(){return(e=Object(d.a)(s.a.mark((function e(){var t;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,L.a.get("".concat(ge,"/customer/").concat(Se));case 2:t=e.sent,j(t.data);case 4:case"end":return e.stop()}}),e)})))).apply(this,arguments)}Se&&function(){e.apply(this,arguments)}()}),[]),Object(P.jsx)(_e.a,{theme:ye,children:Object(P.jsxs)("div",{className:"App container",children:[Object(P.jsxs)(f.a,{position:"sticky",color:"default",children:[Object(P.jsxs)(p.a,{value:n,onChange:function(e,t){r(t)},variant:"scrollable",scrollButtons:"on",indicatorColor:"secondary",textColor:"primary","aria-label":"scrollable force tabs example",children:[Object(P.jsx)(m.a,{label:"Home",icon:Object(P.jsx)(h.a,{})}),Object(P.jsx)(m.a,{label:"My Fridge",icon:Object(P.jsx)(S.a,{})}),Object(P.jsx)(m.a,{label:"About",icon:Object(P.jsx)(y.a,{})}),Object(P.jsx)(m.a,{label:"Log In",icon:Object(P.jsx)(C.a,{})})]}),l&&Object(P.jsx)(v.a,{className:"avatar",alt:l.user_name,src:l.picture})]}),Object(P.jsx)(Ee,{value:n,index:0,children:Object(P.jsx)(D,{})}),Object(P.jsx)(Ee,{value:n,index:1,children:Object(P.jsx)(xe,{})}),Object(P.jsx)(Ee,{value:n,index:2,children:Object(P.jsx)(w,{})}),Object(P.jsx)(Ee,{value:n,index:3,children:Object(P.jsx)(k,{})})]})})},Te=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,213)).then((function(t){var n=t.getCLS,c=t.getFID,a=t.getFCP,r=t.getLCP,i=t.getTTFB;n(e),c(e),a(e),r(e),i(e)}))};i.a.render(Object(P.jsx)(a.a.StrictMode,{children:Object(P.jsx)(Ce,{})}),document.getElementById("root")),Te()},69:function(e,t,n){}},[[150,1,2]]]);
//# sourceMappingURL=main.55a32b27.chunk.js.map