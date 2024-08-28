import { useEffect } from "react";
import { motion, stagger, useAnimate } from "framer-motion";
import { cn } from "../../utils/cn";
import { nord } from "../../Constants";

export const TextGenerateEffect = ({
  words,
  wd="100%",
  className,
  sDelay = 0,
  fSize = 16,
  lHeight = fSize + "px",
  col = "",
  bold = true,
  setGen = null,
}) => {
  const [scope, animate] = useAnimate();
  let len1 = words.length;

  let len2 = words.trim().length;
  const diff = len1 - len2;
 
  let wordsArray = words.trim().split(" ");

  if (
    (wordsArray[0].indexOf(".") != -1 &&
    "1234567890".indexOf(wordsArray[0][0]) != -1)||(wordsArray[0]=="*" || wordsArray[0]=="-")
  ) {
    wordsArray[0] = "•";
  }
  if (wordsArray[0] == "") {
    wordsArray.shift();
  }
  if (len1 != len2) {

    let xx=""
    for (let i = 0; i < len1 - len2; i++) {
      xx+="\t";
    }

    wordsArray[0] = xx + wordsArray[0];
  }
  if (wordsArray.length == 0) return <></>;
  useEffect(() => {
    animate(
      "span",
      {
        opacity: [setGen!=false ? 0 : 1, 1],
        display: [setGen ? "none" : "", ""],
      },
      {
        duration: 2,
        delay: stagger(0.1, { startDelay: 0.1 * sDelay }),
      }
    );
  }, [scope.current]);
  let bold2=false
  let checkbold=(word)=>
    { let val=bold2
      if(word.indexOf("**")!=-1)  {
        
        
        bold2=!bold2
        val=true
        if(word.replace("**","").indexOf("**",2)!=-1) 
        {bold2=!bold2
          val=!bold2
        }
        
      }    
      return val
    }
  const renderWords = () => {
    return (
      <motion.div ref={scope} className="">
        {wordsArray.map((word, idx) => {
          return (
            <motion.span
              key={word + idx}
              className="dark:text-slate-200  text-black opacity-0 "
              style={{ color: col }}
            >
              {checkbold(word)?<b className=" text-sky-100"  style={{color: nord.light.a, fontSize: fSize+2, lineHeight: lHeight }}>{word.replace("**","").replace("**","")}</b>:word.replace("**","") }{" "}
            </motion.span>
          );
        })}
      </motion.div>
    );
  };
  let count=0
  while(wordsArray[0].indexOf("\t")!=-1){
    count++
    wordsArray[0]=wordsArray[0].replace("\t","")
  }
  return (
    <div
      className={
        cn(bold ? "font-bold" : " break-words   font-normal " +wd, className)
      }
      style={{ width: wd,marginLeft:16+(diff+count+(wordsArray[0]=="•"?1:0))*10, paddingRight:16+(diff+count)*10}}
    >
      <div className="mt-4">
        <div
          className=" dark:text-white w-full text-black text-2xl leading-snug tracking-wide"
          style={{ fontSize: fSize, lineHeight: lHeight }}
        >
          {renderWords()}
        </div>
      </div>
    </div>
  );
};
