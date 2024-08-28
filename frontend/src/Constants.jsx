import { io } from "socket.io-client";
import { TextGenerateEffect } from "./components/ui/text-generate-effect";
import { useEffect, useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faTwitter,
  faLinkedin,
  faFacebookF,
  faInstagram,
  faMedium,
} from "@fortawesome/free-brands-svg-icons";
import {  faCircleInfo } from "@fortawesome/free-solid-svg-icons";
const URL = process.env.NODE_ENV === "production" ? undefined : "http://localhost:5000";
export const socket = io(URL, { autoConnect: false });

const nord = {
  dark: {
    a: "#2E3440",
    b: "#3B4252",
    c: "#434C5E",
    d: "#4C566A",
    e: "#424556",
  },
  light: {
    a: "#D8DEE9",
    b: "#E5E9F0",
    c: "#ECEFF4",
  },
  frost: { a: "#8FBCBB", 
    b: "#88C0D0", 
    c: "#81A1C1", 
    d: "#5E81AC" 
  },
  color: {
    r: "#BF616A",
    o: "#D08770",
    y: "#EBCB8B",
    g: "#A3BE8C",
    p: "#B48EAD",
  },
};

let logoColors = ["#f3982b", "#148336", "#4f4678", "#b21d2a"];
let logoText = Array.from("TEKGEMINUS");
let logo = logoText.map((letter, index) => (
  <span
    key={index}
    className={"text-[34px] select-none " + (index > 5 ? letter : " ")}
    style={{
      fontFamily: "CustomFont",
      letterSpacing: index == 0 ? "-1px" : "-2px",
      color: index > 5 ? logoColors[index - 6] : "#ddd",
    }}
  >
    {letter}
  </span>
));

let greetingText = ["Hello,", "How may I help you?"];
let greeting = (
  <>
    <TextGenerateEffect
      words={greetingText[0]}
      className="mt-[35vh] duration-500 greet font-mono text-3xl text-start"
      col={nord.light.a}
      sDelay={7}
      fSize={32}
    ></TextGenerateEffect>
    <TextGenerateEffect
      words={greetingText[1]}
      className=" font-mono  duration-500 greet text-3xl justify-start text-start"
      col={nord.light.a}
      sDelay={13}
      fSize={32}
    ></TextGenerateEffect>
  </>
);

let getWindowDimensions = () => {
  const { innerWidth: width, innerHeight: height } = window;
  return {
    width,
    height,
  };
};
export  function useWindowDimensions() {
  const [windowDimensions, setWindowDimensions] = useState(
    getWindowDimensions()
  );

  useEffect(() => {
    function handleResize() {
      setWindowDimensions(getWindowDimensions());
    }

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return windowDimensions;
}

const placeholder = [
  "Type a message...",
  "What is customer information?",
  "What is Start/Stop Flexibility?",
  "How do I change my password?",
  "How do I create an account?",
];

const socials=<>
<a target="_blank" href="https://twitter.com/TGeminus">
  <FontAwesomeIcon
    className=" brightness-50 hover:brightness-100 duration-300"
    icon={faTwitter}
    key="74"
  />
</a>
<a
  target="_blank"
  href="https://www.facebook.com/TekGeminus-103615787761244/"
>
  <FontAwesomeIcon
    className=" brightness-50 hover:brightness-100 duration-300"
    icon={faFacebookF}
    key="97"
  />
</a>
<a
  target="_blank"
  href="https://www.linkedin.com/company/tekgeminus/about/"
>
  <FontAwesomeIcon
    className=" brightness-50 hover:brightness-100 duration-300"
    icon={faLinkedin}
    key="116"
  />
</a>
<a target="_blank" href="https://www.instagram.com/tekgeminus/">
  <FontAwesomeIcon
    className=" brightness-50 hover:brightness-100 duration-300"
    icon={faInstagram}
    key="_97"
  />
</a>
<a target="_blank" href="https://medium.com/@tekgeminus">
  <FontAwesomeIcon
    className=" brightness-50 hover:brightness-100 duration-300"
    icon={faMedium}
    key="110"
  />
</a>
</>
const info=<>
<FontAwesomeIcon className="h-5" icon={faCircleInfo} />

<div
  className=" text-center shadow-md font-mono w-64 absolute gap-2 group-hover:scale-100 flex flex-col scale-50 mt-1  opacity-0 group-hover:delay-500  ease-out  right-0 rounded-md  duration-300   group-hover:opacity-90 p-5 leading-5"
  style={{ backgroundColor: nord.dark.b + "60" }}
>
  {/*["#f3982b", "#148336", "#4f4678", "#b21d2a"]; */}
  <div style={{ fontFamily: "myFirstFont", fontSize: "24px" }}>
    <label>
      TEK
      <label className="text-[#f3982b] ">H</label>
      <label className="text-[#148336] ">E</label>
      <label className="text-[#4f4678] ">L</label>
      <label className="text-[#b21d2a] ">P</label>
    </label>
  </div>
  <div className=" w-full  items-center justify-between flex">
    <label>Version :</label>
    <label>v0.1</label>
  </div>
  <div className="flex mt-2 flex-col">
    <p className="fadein text-sm" style={{ color: nord.light.a }}>
      {" "}
      All rights reserved.
    </p>
    <p className="fadein    text-sm" style={{ color: nord.light.a }}>
      {" "}
      © 2024{" "}
      <a href="https://www.tekgeminus.com/" target="_blank">
        Tekgeminus Solutions
      </a>{" "}
      (P) Ltd.{" "}
    </p>
  </div>
</div>
</>
export { nord, logo, greeting, placeholder,socials,info};
