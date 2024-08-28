import Dots from "./Dots";
import "./MessageDisplay.css";
import { nord } from "../Constants";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faRobot,
  faUser,
  faCopy,
  faCheck,
  faFileArrowDown,
  faArrowsRotate,
  faCaretDown,
} from "@fortawesome/free-solid-svg-icons";
import { TextGenerateEffect } from "./ui/text-generate-effect";
import { useState } from "react";

let isSpinning = false; //to control the spinning of the regenerate icon
let messageCache = { index: [], message: [] }; //to store the formatted messages

export let resetCache = () => {
  //to reset the cache on activeChatIndex change
  messageCache = { index: [], message: [] };
};

function MessageDisplay(props) {
  const [open, setOpen] = useState(props.chat.map(() => false)); //to control the expansion of the source
  const [spin, setSpin] = useState(0); //to control the degree of rotation of the regenerate icon

  let spinner = async () => {
    //using this instead of default fontAwesome animation to control the degree of rotation, can be replaced with default animation
    await new Promise((r) => setTimeout(r, 500));
    while (isSpinning) {
      setSpin((spin) => (spin + 5) % 360);
      await new Promise((r) => setTimeout(r, 20));
    }
  };

  let formatResponse = (msg, ind) => {
    //to format the response message

    if (messageCache.index.includes(ind)) {
      //if the message is already formatted, return the formatted message
      return messageCache.message[messageCache.index.indexOf(ind)];
    } else if (msg == "") {
      return <></>; //if the message is empty, return an empty element
    }

    let lineArray = msg.split("\n");
    let sepcialFormating = { start: [], end: [], content: [], type: [] }; //to store the special formatting like code and table, bold is handled by the TextGenerateEffect component
    let tableStart = -1;
    let tableEnd = -1;
    let start = -1;
    let end = -1;

    for (let i = 0; i < lineArray.length; i++) {
      //to find the special formatting like code and table and store them in sepcialFormating
      let trimmed = lineArray[i].trim();
      if (trimmed.split(" ").length == 1 && trimmed.slice(0, 3) == "```") {
        if (start == -1) {
          start = i;
        } else {
          end = i;
          sepcialFormating.start.push(start);
          sepcialFormating.end.push(end);
          sepcialFormating.content.push(lineArray.slice(start, end));
          sepcialFormating.type.push("code");
          start = -1;
          end = -1;
        }
      } else if (start != -1 && i == lineArray.length - 1) {
        end = i;
        sepcialFormating.start.push(start);
        sepcialFormating.end.push(end);
        sepcialFormating.content.push(lineArray.slice(start, end));
        sepcialFormating.type.push("code");
        start = -1;
        end = -1;
      }
      if (
        trimmed[0] == "|" &&
        trimmed[trimmed.length - 1] == "|" &&
        tableStart == -1
      ) {
        tableStart = i;
      } else if (
        tableStart != -1 &&
        ((trimmed[0] != "|" && trimmed[trimmed.length - 1] != "|") ||
          i == lineArray.length - 1)
      ) {
        tableEnd = i;
        if (i == lineArray.length - 1) tableEnd += 1;
        sepcialFormating.start.push(tableStart);
        sepcialFormating.end.push(tableEnd);
        sepcialFormating.content.push([
          lineArray[tableStart],
          lineArray.slice(tableStart + 2, tableEnd),
        ]);
        sepcialFormating.type.push("table");
        tableStart = -1;
        tableEnd = -1;
      }
    }

    let ArrayLineArray = [];
    for (let i = 0; i < sepcialFormating.start.length; i++) {
      //to create the formatted message
      if (sepcialFormating.start[i] != 0 && i == 0) {
        ArrayLineArray.push({
          type: "text",
          lines: lineArray.slice(0, sepcialFormating.start[i]),
        });
      } else if (i != 0)
        ArrayLineArray.push({
          type: "text",
          lines: lineArray.slice(
            sepcialFormating.end[i - 1] + 1,
            sepcialFormating.start[i]
          ),
        });
      ArrayLineArray.push({
        type: sepcialFormating.type[i],
        lines: sepcialFormating.content[i],
      });
      if (i == sepcialFormating.start.length - 1) {
        ArrayLineArray.push({
          type: "text",
          lines: lineArray.slice(sepcialFormating.end[i] + 1),
        });
      }
    }

    if (ArrayLineArray.length == 0) {
      //if there is no special formatting
      ArrayLineArray.push({ type: "text", lines: msg.split("\n") });
    }

    let tally = 0; //to calculate the delay for the TextGenerateEffect component
    let tallyLineLength = (x) => {
      tally += x;
      return tally - x;
    };

    let formattedElementList = ArrayLineArray.map((rootLines, inde) => {
      //to create the formatted message

      if (rootLines.type == "text") {
        //normal text
        return rootLines.lines.map((line, index) => (
          <TextGenerateEffect
            key={index + "line" + ind + " " + inde}
            sDelay={tallyLineLength(line.split(" ").length)}
            words={line}
            lHeight={"22px"}
            fSize={18}
            setGen={props.cd}
            bold={false}
            wd={"w-[90%]  xl:w-[40vw]"}
            className="text-white break-words "
          ></TextGenerateEffect>
        ));
      } else if (rootLines.type == "code") {
        //code
        return (
          <div
            className="text-white  shadow-md   bg-[#252c38] flex flex-col rounded-md my-8  opacity-100   text-lg w-[90%]  xl:w-[40vw] "
            style={{
              animation: !props.cd
                ? ""
                : "second " +
                  tally * 0.1 +
                  "s , temptest 0.5s " +
                  tally * 0.1 +
                  "s",
            }}
          >
            <div className=" bg-[#3B4252] text-slate-200 rounded-t-md leading-10 pl-2 text-sm w-full h-10">
              {
                rootLines.lines[0]
                  .trim()
                  .slice(
                    3
                  ) // Removes ``` from the start, usually followed by language name like python, sql, c++ etc. 
              }
            </div>
            {rootLines.lines.slice(1).map((line, index) => (
              <TextGenerateEffect
                key={index + "line" + ind + " " + inde}
                sDelay={tallyLineLength(line.split(" ").length)}
                words={line}
                lHeight={"20px"}
                fSize={16}
                setGen={props.cd}
                bold={false}
                wd={"w-[90%]  xl:w-[40vw]"}
                className="text-white "
              ></TextGenerateEffect>
            ))}
            <div className="  text-slate-200 mt-2 flex items-end justify-end  gap-2 pr-[1%] rounded-b-md leading-5 text-sm w-full h-0">
              <div className="group group self-end sticky text-[#B3BCCE]">
                <FontAwesomeIcon
                  id="copy"
                  onClick={(e) => {
                    //copy to clipboard

                    document.getElementById("copy").style.display = "none";
                    document.getElementById("check").style.display = "";
                    setTimeout(() => {
                      document.getElementById("check").style.display = "none";
                      document.getElementById("copy").style.display = "";
                    }, 1000);

                    let copyText = rootLines.lines;
                    copyText.shift();
                    copyText = copyText.join("\n");
                    navigator.clipboard.writeText(copyText);
                  }}
                  className="bg-[#3B4252] group-hover:text-white duration-300 h-4 aspect-square leading-3 rounded-md text-center p-2"
                  icon={faCopy}
                />
                <FontAwesomeIcon
                  id="check"
                  style={{ display: "none" }}
                  className="bg-[#3B4252]  text-green-200 duration-300 h-4 aspect-square leading-3 rounded-md text-center p-2"
                  icon={faCheck}
                />
                <p
                  className=" text-center absolute group-hover:scale-100  scale-50  opacity-0 group-hover:delay-500  ease-out  -right-[0.6rem] rounded-md group-hover:block duration-300 text-sm  group-hover:opacity-90 p-1 px-2 leading-5"
                  style={{ backgroundColor: nord.dark.b }}
                >
                  Copy
                </p>
              </div>

              <div className="group self-end sticky  text-[#B3BCCE]">
                <FontAwesomeIcon
                  onClick={(e) => { //download the code
                    let copyText = rootLines.lines;
                    copyText.shift();
                    copyText = copyText.join("\n");
                    const link = document.createElement("a");
                    const file = new Blob([copyText], { type: "text/plain" });
                    link.href = URL.createObjectURL(file);
                    link.download = "download.txt"; //change the file extension according to the language in the future
                    link.click();
                    URL.revokeObjectURL(link.href);
                  }}
                  className="bg-[#3B4252] group-hover:text-white duration-300 h-4 aspect-square group leading-3 rounded-md text-center p-2"
                  icon={faFileArrowDown}
                />
                <p
                  className=" text-center absolute group-hover:scale-100  scale-50  opacity-0 group-hover:delay-500  ease-out  -right-6 rounded-md group-hover:block duration-300 text-sm  group-hover:opacity-90 p-1 px-2 leading-5"
                  style={{ backgroundColor: nord.dark.b }}
                >
                  Download
                </p>
              </div>
            </div>
          </div>
        );
      } else { //tables
        return (
          <>
            <div
              className="text-white p-[1px] shadow-md bg-[rgb(37,44,56)] flex flex-col rounded-md my-8  opacity-100  text-lg max-w-[90%]  xl:max-w-[40vw] "
              style={{
                animation: !props.cd
                  ? ""
                  : "second " +
                    tally * 0.1 +
                    "s , temptest 1s " +
                    tally * 0.1 +
                    "s",
              }}
            >
              <table className="rounded-sm ">
                <thead>
                  <tr>
                    {rootLines.lines[0]
                      .slice(1, rootLines.lines[0].length - 1)
                      .split("|")
                      .map((hd) => (
                        <th className="text-lg">{hd.trim()}</th>
                      ))}
                  </tr>
                </thead>
                <tbody>
                  {rootLines.lines[1]
                    .map((ll) => ll.slice(1, ll.length - 1).split("|"))
                    .map((ro) => (
                      <tr>
                        {ro.map((ele, ind) => (
                          <td
                            className=" pl-2 pr-2   text-base"
                            style={{ textAlign: ind > 0 ? "left" : "left" }}
                          >
                            {ele.trim()}
                          </td>
                        ))}
                      </tr>
                    ))}
                </tbody>
              </table>
            </div>
          </>
        );
      }
    });

    messageCache.index.push(ind); //store the formatted message index in the cache
    messageCache.message.push(formattedElementList); //store the formatted message in the cache

    return formattedElementList;
  };

  let history = props.chat.filter((msg) => {
    return msg.type != "newchat";
  }); //filter the chat to remove the newchat message

  history = history.map((msg, index) => (
    <div
      style={{
        justifyContent: msg.type == "query" ? "flex-end" : "flex-start",
      }}
      className={
        " items-center flex duration-300 flex-row gap-2 p-2 pb-4 w-full  rounded-md justify-end fadein "
      }
      key={msg.message + (props.chat.length - index)}
    >
      {/*Bot Icon*/}
      <div
        className="h-10 aspect-square bg-white  pl-[9px]  rounded-full  "
        style={{
          backgroundColor: nord.dark.c,
          display: msg.type == "query" ? "none" : "block",
          lineHeight: "40px",
        }}
      >
        <FontAwesomeIcon icon={faRobot} />
      </div>

      {/*Waiting Dots*/}
      {msg.message == "" ? <Dots /> : <></>}

      {/*Message*/}
      <div className="w-[calc(100%-88px)]    justify-end flex flex-col">
        {/*Content*/}
        <div
          className=" w-full "
          style={{
            alignSelf: msg.type == "query" ? "flex-end" : "flex-start",
            textAlign: msg.type == "query" ? "right" : "left",
          }}
        >
          {msg.type == "query" ? (
            msg.message.split("\n").map((line, ind) => (
              <p
                key={props.chat.length - index + "" + ind}
                style={{
                  color: msg.type == "query" ? nord.light.a : nord.light.c,
                }}
                className="w-full"
              >
                {line}
              </p>
            ))
          ) : (
            <div className="duration-300">
              {" "}
              {formatResponse(msg.message, props.chat.length - index)}
            </div>
          )}
        </div>

        {/*Source*/}
        {msg.message == "" || msg.type == "query" ? (
          <></>
        ) : (
          <>
            <div
              id="src"
              className={
                " text-sm mt-2 w-[calc(100%-32px)]  overflow-hidden overflow-ellipsis " +
                (open[props.chat.length - index] ? " break-words" : "")
              }
              style={{ color: "#838C9E" }}
            >
              Source:
              {open[props.chat.length - index] ? (
                msg.reference.map((src, inx) => (
                  <p className="break-words" key={inx}>
                    {src}
                  </p>
                ))
              ) : (
                <p className=" overflow-hidden overflow-ellipsis">
                  {msg.reference[0]}
                </p>
              )}
            </div>

            {/*Regenerate Response*/}
            <div
              onClick={props.regen}
              className="h-10   sticky -mr-5    mb-10 self-end  text-[#B3BCCE]   -mt-20  hover:scale-100  aspect-square duration-300  w-fit flex flex-col items-center justify-center group opacity-100"
              style={{
                display: index != 0 || msg.message == "" ? "none" : "block",
                lineHeight: "40px",
                opacity: "1",
              }}
              onMouseEnter={(e) => {
                isSpinning = true;
                spinner();
              }}
              onMouseLeave={(e) => {
                isSpinning = false;
              }}
            >
              <FontAwesomeIcon
                className="w-full  transition-colors group-hover:text-white duration-300 text-center"
                icon={faArrowsRotate}
                style={{ transform: `rotate(${spin}deg)` }}
              />
              <p
                className=" text-center absolute group-hover:scale-100  scale-50  opacity-0 group-hover:delay-500  ease-out  -right-7 rounded-md group-hover:block duration-300 text-sm  group-hover:opacity-90 p-1 px-2 leading-5"
                style={{ backgroundColor: nord.dark.b }}
              >
                Regenerate
              </p>
            </div>
            <div
              className="h-10 w-10 hover:scale-100  duration-300 -mr-5   -mt-8 text-[#B3BCCE]   self-end group opacity-100"
              onClick={(e) => {
                let opC = JSON.parse(JSON.stringify(open));
                opC[props.chat.length - index] =
                  !opC[props.chat.length - index];
                setOpen(opC);
              }}
            >
              <FontAwesomeIcon
                className=" duration-300 group-hover:text-white  text-center w-full  "
                icon={faCaretDown}
                rotation={open[props.chat.length - index] ? 180 : 0}
              />
              <p
                className={
                  " text-center absolute  group-hover:scale-100  transition-[opacity,transform] scale-50  opacity-0  group-hover:delay-500  ease-out " +
                  (open[props.chat.length - index] ? "-right-5" : "-right-3") +
                  " rounded-md group-hover:block duration-300 text-sm  group-hover:opacity-90 p-1 px-2 leading-5"
                }
                style={{ backgroundColor: nord.dark.b }}
              >
                {open[props.chat.length - index] ? "Collapse" : "Expand"}
              </p>
            </div>
          </>
        )}
      </div>

      {/*User Icon*/}
      <div
        className="h-10 aspect-square bg-white pl-[12px] rounded-full  "
        style={{
          backgroundColor: nord.dark.c,
          display: msg.type == "query" ? "block" : "none",
          lineHeight: "40px",
        }}
      >
        <FontAwesomeIcon icon={faUser} />
      </div>
    </div>
  ));
  return <>{history}</>;
}

export default MessageDisplay;
