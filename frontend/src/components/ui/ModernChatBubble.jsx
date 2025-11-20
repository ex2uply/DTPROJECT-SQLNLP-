import { motion } from "framer-motion";
import { cn } from "../../lib/utils";

export default function ModernChatBubble({ isUser, message, timestamp }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10, scale: 0.95 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{ duration: 0.3 }}
      className={cn(
        "flex w-full mb-4",
        isUser ? "justify-end" : "justify-start"
      )}
    >
      <div
        className={cn(
          "max-w-[80%] px-6 py-4 rounded-2xl backdrop-blur-md shadow-lg",
          isUser
            ? "bg-gradient-to-br from-blue-600 to-purple-600 text-white rounded-tr-sm"
            : "bg-white/10 border border-white/10 text-gray-100 rounded-tl-sm"
        )}
      >
        <p className="text-base leading-relaxed">{message}</p>
        {timestamp && (
          <p className={cn("text-xs mt-2 opacity-60", isUser ? "text-blue-100" : "text-gray-400")}>
            {timestamp}
          </p>
        )}
      </div>
    </motion.div>
  );
}
