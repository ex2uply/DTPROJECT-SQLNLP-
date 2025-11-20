import { motion } from "framer-motion";
import { cn } from "../../lib/utils";

export default function GlassCard({ children, className, hoverEffect = false }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={hoverEffect ? { scale: 1.02, boxShadow: "0 20px 40px rgba(0,0,0,0.2)" } : {}}
      transition={{ duration: 0.4, ease: "easeOut" }}
      className={cn(
        "bg-black border border-white/20 rounded-lg shadow-sm overflow-hidden",
        className
      )}
    >
      {children}
    </motion.div>
  );
}
