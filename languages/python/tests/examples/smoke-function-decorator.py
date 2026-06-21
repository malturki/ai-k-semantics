#defArgs(one, #noIds, {
return 1;
});
#defArgs(two, #noIds, {
return 2;
});
#def(first, f, {
return one;
});
#def(second, f, {
return two;
});
#defDecorated(target, #args(first, #arg(second)), #functionArgs(#noIds, {
return 0;
}));
targetResult = #call(target, #noArgs);
#def(identity, f, {
return f;
});
#defDecorated(defaulted, #arg(identity), #functionDefaults(#id(x), #arg(12), {
return x;
}));
(targetResult == 1) and (#call(defaulted, #noArgs) == 12);
