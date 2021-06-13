import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Register from "./components/Register";
import Login from "./components/Login";
import Logout from "./components/Logout";
import Single from "./components/Single";
import Search from "./components/Search";
import Admin from "./Admin";
import Create from "./components/admin/create";
import Delete from "./components/admin/delete";
import Edit from "./components/admin/edit";
import { AnimatePresence } from "framer-motion"
const routing = (
  <Router>
    <React.StrictMode>
      <Header />
      <AnimatePresence initial={false} exitBeforeEnter>
      <Switch>
        <Route path="/" exact component={App} />
        <Route exact path="/admin" component={Admin} />
        <Route exact path="/admin/create" component={Create} />
        <Route exact path="/admin/edit/:id" component={Edit} />
        <Route exact path="/admin/delete/:id" component={Delete} />
        <Route path="/register" component={Register} />
        <Route path="/login" component={Login} />
        <Route path="/logout" component={Logout} />
        <Route exact path="/post/:slug" component={Single} />
        <Route path="/search" component={Search} />
      </Switch>
      </AnimatePresence>
      <Footer />
    </React.StrictMode>
  </Router>
);

ReactDOM.render(routing, document.getElementById("root"));
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
