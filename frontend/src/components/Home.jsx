import { useEffect, useState } from "react";
import {
  nord,
  socket,
  logo,
  greeting,
  placeholder,
  useWindowDimensions,
  info,
  socials
} from "../Constants";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPaperPlane } from "@fortawesome/free-solid-svg-icons";
import MessageDisplay, { resetCache } from "./MessageDisplay";
import { AnimatePresence, motion } from "framer-motion";
import { FlipWords } from "./ui/flipwords";


let statelessMessages = []; //stores the messages of active chat
let chatStore = []; //stores the messages of all the chats
let chatTypeStore = [0]; //stores the type of chat
let types = ["CAbout 2M", "About Database", "Configuration Help"]; //types of chat


function Home() {

  const { height, width } = useWindowDimensions(); //get the window dimensions
  const [received, setReceived] = useState(true); //to check if the response is received
  const [cSHeight, setcSHeight] = useState("28px"); //height of the chat box
  const [activeChatIndex, setActiveChatIndex] = useState(0); //index of the active chat
  const [chatType, setChatType] = useState(0); //type of the active chat
  const [messages, setMessages] = useState([]); //messages of the active chat
  const [sendButtonKey, setSendButtonKey] = useState(0); //key to animate the send button
  const [switched, setSwitched] = useState(false); //to check if the chat recently is switched

  
  useEffect(() => { //to update the messages of the active chat in chatStore
    chatStore[activeChatIndex] = messages;
  }, [messages]); 


  useEffect(() => { 
    socket.on("response", (data) => { //to update messages of the active chat when response is received
      statelessMessages[0] = {
        type: "response",
        message: data.response,
        reference: data.reference,
      };
      setMessages(statelessMessages);
      setReceived(true);
      socket.disconnect();
    });
  }, [activeChatIndex]);


  const sendMessage = async (chatbox) => { 
    socket.connect(); 
    setSwitched(false); 
    setSendButtonKey((sendButtonKey + 1) % 100); 
    setReceived(false); 

    const dataToSend = { 
      history: JSON.parse(JSON.stringify(messages)).reverse(),
      query: chatbox.value,
      chatIndex: activeChatIndex,
      chatType: chatType,
    };

    console.log("Sending event 'query' with data:", dataToSend); 

    socket.emit("query", dataToSend);


    //console.log("Sent message: ",chatbox.value)
    
    statelessMessages = JSON.parse( //update the messages of the active chat
      JSON.stringify([
        {
          type: "response",
          message: "",
        },
        { type: "query", message: chatbox.value },
        ...messages,
      ])
    );
    setMessages(statelessMessages); //set the messages of the active chat
    chatbox.value = ""; //clear the chat box
    chatbox.style.height = "28px"; //set the height of the chat box
    setcSHeight("0px");
    await new Promise((r) => setTimeout(r, 300000));
    setcSHeight("28px");
  };


  const regenerate = () => { //to regenerate the response
    socket.connect();
    socket.emit("query", {
      history: messages,
      query: "That Doesn't seem right, regenerate the response",
      chatIndex: activeChatIndex,
    });
    statelessMessages = JSON.parse(
      JSON.stringify([{ type: "response", message: "" }, ...messages])
    );
    setMessages(statelessMessages);
  };


  let typeSelect = types.map((type, index) => { //to display the chat type selector
    return (
      <div
        key={"typeSelect " + index}
        className="w-full hover:brightness-110 brightness-95 hover:scale-[1.025] text-xl flex flex-col items-center select-none cursor-pointer text-center font-mono shadow-xl xl:text-ellipsis xl:overflow-hidden xl:whitespace-nowrap  text-white pt-3 gap-1 pb-2 duration-300 my-2  h-fit rounded-md"
        style={{
          backgroundColor: nord.dark.b,
          outline: "solid",
          outlineColor: chatType == index ? nord.light.a : nord.dark.c,
          outlineWidth: "1px",
        }}
        onClick={() => {
          setChatType(index);
          console.log("Index number is :", index)
          chatTypeStore[activeChatIndex] = index;
        }}
      >

        <label className=" pointer-events-none">{type}</label>
        <label className="text-base pointer-events-none">Description</label>

      </div>
    );
  });


  let chatTitle = [];
  for (let i = 0; i < chatStore.length; i++) { //to display the chat chatTitle
    try {
      chatTitle.push(
        <div
          key={"chatSelect " + i}
          className=" fadein w-full flex items-center justify-start text-xl hover:scale-[1.025] pl-2 text-start font-mono hover:brightness-110 brightness-95 duration-300 shadow-xl cursor-pointer  text-white leading-[3.7rem] my-2 h-16 rounded-md"
          style={{
            backgroundColor: nord.dark.b,
            outline: "solid",
            outlineColor: activeChatIndex == i ? nord.light.a : nord.dark.c,
            outlineWidth: "1px",
          }}
          onClick={() => {
            if (!received) return;
            resetCache(i);
            setSwitched(true);
            setChatType(chatTypeStore[i]);
            setMessages(chatStore[i]);
            setActiveChatIndex(i);
          }}
        >

          <div className="w-11/12 text-ellipsis overflow-hidden whitespace-nowrap">
            {
              chatStore[i].filter((ex_chat) => {
                return ex_chat.type != "response";
              })[0].message
            }
          </div>

        </div>
      );
    } catch (e) {}
  }


  return (
    <>
      {" "}
      {/*Name List with + New Chat */}
      <div
        className={
          " w-[25%] hidden xl:block overflow-x-hidden p-32 px-16 z-[0]  h-full  overflow-y-scroll items-start  duration-300  absolute "
        }
        style={{}}
      >
        {chatTitle}
        <div  //New Chat Button
          onClick={(e) => {
            if (!received) return;

            chatStore.push([]);
            chatTypeStore.push(0);
            for (let i = 0; i < chatStore.length - 1; i++) {
              chatStore[chatStore.length - 1].push({
                type: "newchat",
                message: "New Chat",
              });
            }
            resetCache(chatStore.length - 1, true);
            setMessages(chatStore[chatStore.length - 1]);
            setActiveChatIndex(chatStore.length - 1);
            setChatType(0);
          }}
          className={
            "w-full cursor-pointer flex gap-2 pb-2 justify-center overflow-x-hidden my-2 h-16 text-center rounded-md  " +
            (messages.length > 0 ? "fadein" : "opacity-0")
          }
          style={{
            outline: "solid",
            outlineWidth: "1px",
            outlineColor: nord.dark.c,
            color: nord.light.a,
          }}
        >
          {" "}
          <label className="text-5xl text-center h-full leading-[3.5rem]">
            +{" "}
          </label>{" "}
          <label className=" text-xl text-center h-full leading-[3.5rem]">
            New Chat
          </label>
        </div>
      </div>
      <div
        className={
          "h-full w-[96%] ml-[2%] xl:w-1/2 xl:left-[23%] pb-10 duration-300 absolute items-center gap-2 flex flex-col-reverse"
        }
      >


        {/*Bottom Fadeout*/}
        <div
          style={{
            backgroundImage:
              "linear-gradient(180deg, rgba(46, 52, 64,0) 0%," +
              nord.dark.a +
              " 75%, " +
              nord.dark.a +
              " 100%)",
            marginBottom: "calc(" + cSHeight + " - 28px)",
          }}
          className="w-[100vw] z-[9999]  p-32 bottom-0 left-0 fixed duration-300 pointer-events-none"
        />


        {/*Message Box*/}
        <div
          className="mbox duration-300  z-[9999] w-full h-fit h-min-[3vmax] max-h-[calc(30vh+1.5rem)] px-1 py-3 absolute shadow-xl rounded-xl items-center justify-end flex  font-mono text-lg "
          style={{
            backgroundColor: nord.dark.b,
            color: nord.light.a,
            marginBottom:
              messages.length == 0 && cSHeight == "28px" && width > "1279"
                ? "28vh"
                : "0px",
            width: messages.length == 0 && width > "1279" ? "70%" : "100%",
          }}
        >

          <textarea
            id="chat"
            row="1"
            type="text"
            placeholder={"Type a message..."}
            rows="1"
            className="w-full max-h-[30vh] min-h-[28px]  mx-2 mt-[0.325rem] my-auto mr-[5%]  resize-none scrollbar-hide text-lg"
            onKeyDown={(e) => {
              if (e.key == "Enter" && !e.shiftKey) {
                let chatbox = document.getElementById("chat");
                e.preventDefault();
                if (chatbox.value.length > 0 && received) {
                  sendMessage(chatbox);
                }
              }
            }}
            onFocusCapture={(e) => {
              //to hide the placeholder on focus
              document.getElementById("placeholder").style.opacity = "0";
            }}
            onBlurCapture={(e) => {
              //to show the placeholder on blur
              if (e.target.value.length == 0) {
                document.getElementById("placeholder").style.opacity = "1";
              }
            }}
            onInput={(e) => {
              //resize the text box (up to 1/2 screen height) as the user types
              let chat = document.getElementById("chat");
              chat.style.height = "28px";
              chat.style.height = chat.scrollHeight + "px";
              setcSHeight(chat.style.height);
              chat.style.maxHeight = "30vh";
            }}
            style={{ background: "none", outline: "none" }}
          />

          {/*Send button (Paper Plane) animation on click/enter to send query*/}
          <AnimatePresence>

            <motion.div
              key={sendButtonKey}
              initial={{
                opacity: 0,
                y: 10,
                filter: "blur(8px)",
              }}
              animate={{
                opacity: 1,
                y: 0,
                filter: "blur(0px)",
              }}
              transition={{
                duration: 0.5,
                ease: "easeInOut",
              }}
              exit={{
                opacity: 0,
                y: -40,
                x: 40,
                filter: "blur(8px)",
                scale: 2,
                top: "12px",
                position: "absolute",
              }}
              className=" aspect-square h-[40px]  self-end duration-300 text-end  "
              onClick={() => {
                let chatbox = document.getElementById("chat");
                if (chatbox.value.length > 0 && received) {
                  sendMessage(chatbox);
                }
              }}
              style={{ lineHeight: cSHeight, color: nord.light.a }}
            >

              <FontAwesomeIcon
                className="mr-3 mb-3  absolute bottom-0 right-0 pointer-events-none"
                icon={faPaperPlane}
              />

            </motion.div>

          </AnimatePresence>

          {/*Place holder text animation*/}
          <div
            id="placeholder"
            className="w-4/5 h-5/6 left-1 absolute overflow-hidden overflow-ellipsis pointer-events-none duration-300 transition-opacity"
            style={{ backgroundColor: nord.dark.b }}
          >

            <FlipWords
              words={placeholder}
              duration={5000}
              className=" w-full h-full mt-[0.3rem]  text-lg leading-[42px]"
            />

          </div>

        </div>



        {/*Chat Type Selector*/}
        <div
          className="hidden xl:flex absolute gap-5 justify-evenly px-10 bottom-[20vh] left-1/2  -translate-y-1/2 h-12 fadein -translate-x-1/2   xl:w-full "
          style={{
            display:
              messages.filter((x) => {
                return x.type != "newchat";
              }).length > 0
                ? "none"
                : "",
          }}
        >
          {typeSelect}
        </div>


        {/*Chat History*/}
        <div
          className=" w-[calc(100%+10px)] h-full  mb-10 mt-5 ml-[10px] overflow-x-clip overflow-y-scroll   rounded-xl flex flex-col-reverse  font-mono text-lg gap-3"
          id="chatbox"
          style={{
            marginBottom: cSHeight,
            color: nord.light.a,
            transitionDuration: cSHeight == "0px" ? "0s" : "1s",
          }}
        >
          <div className="p-8 w-full rounded-md justify-end" key={-1} />
          <MessageDisplay
            chat={messages}
            cInd={activeChatIndex}
            regen={regenerate}
            cd={!switched}
          />
          <div className="p-12 w-full rounded-md justify-end" key={-2} />
        </div>


        {/*Greeting*/}
        <div
          id={"GRT"}
          className="absolute pointer-events-none glisten z-[9999] overflow-clip  h-full w-fit items-center text-center duration-300 justify-center"
          style={{
            opacity: messages.length == 0 ? "1" : "0",
            display: messages.length == 0 ? "block" : "none",
          }}
        >
          {greeting}
        </div>


        {/*Top Fadeout*/}
        <div
          style={{
            backgroundImage:
              "linear-gradient(0deg, rgba(46, 52, 64,0) 0%," +
              nord.dark.a +
              " 75%, " +
              nord.dark.a +
              " 100%)",
          }}
          className=" pointer-events-none items-center fixed left-0  p-24 top-0 w-[100vw] rounded-md justify-end"
        />


        {/*Logo*/}
        <a
          href="https://www.tekgeminus.com/"
          target="_blank"
          className="logo fixed  xl:left-16 top-2"
        >
          {logo}
        </a>


        {/*Info Icon T-R*/}
        <div className="fadein fixed brightness-50 group hover:brightness-100 duration-300 text-white  right-5 xl:right-16 top-5">
          {info}
        </div>


        {/*Copyright Info B-L */}
        <p
          className="fadein fixed z-[9999]   xl:left-16 bottom-2 text-sm"
          style={{ color: nord.light.c }}
        >

          {" "}
          © 2024{" "}
          <a href="https://www.tekgeminus.com/" target="_blank">
            Tekgeminus Solutions
          </a>{" "}
          (P) Ltd.{" "}

        </p>


        {/*Links to social B-R*/}
        <div
          className="fadein fixed  z-[9999] hidden xl:flex  gap-3 right-16 bottom-2  text-xl"
          style={{ color: nord.light.a }}
        >
          {socials}
        </div>



      </div>
    </>
  );
}

export default Home;
